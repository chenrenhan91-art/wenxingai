#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "hot-news-data.json"
OUTPUT_DIR = ROOT / "generated"
GEMINI_BUNDLE_PATH = OUTPUT_DIR / "gemini-content-bundle.json"
PIPELINE_STATE_PATH = OUTPUT_DIR / "pipeline-state.json"
PIPELINE_REPORT_JSON_PATH = OUTPUT_DIR / "pipeline-report.json"
PIPELINE_REPORT_MD_PATH = OUTPUT_DIR / "pipeline-report.md"


def load_env_files() -> None:
    for filename in (".env.local", ".env"):
        env_path = ROOT / filename
        if not env_path.exists():
            continue
        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_snapshot_signature(payload: dict[str, Any] | None) -> str:
    if not payload:
        return ""
    items = payload.get("items") or []
    compact_items = [
        {
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "source": item.get("source", ""),
            "published": item.get("published", ""),
        }
        for item in items[:8]
    ]
    signature_source = json.dumps(compact_items, ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(signature_source.encode("utf-8")).hexdigest()


def build_bundle_signature(payload: dict[str, Any] | None) -> str:
    if not payload:
        return ""
    items = payload.get("input_items") or []
    compact_items = [
        {
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "source": item.get("source", ""),
            "published": item.get("published", ""),
        }
        for item in items[:8]
    ]
    signature_source = json.dumps(compact_items, ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(signature_source.encode("utf-8")).hexdigest()


def summarize_titles(payload: dict[str, Any] | None) -> list[str]:
    if not payload:
        return []
    return [str(item.get("title", "")).strip() for item in (payload.get("items") or [])[:5] if item.get("title")]


def run_step(script_name: str) -> dict[str, Any]:
    script_path = ROOT / "scripts" / script_name
    process = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    combined_output = "\n".join(part for part in (process.stdout.strip(), process.stderr.strip()) if part)
    return {
        "script": script_name,
        "returncode": process.returncode,
        "ok": process.returncode == 0,
        "output": combined_output,
    }


def render_report(report: dict[str, Any]) -> str:
    lines = [
        f"# 问星AI 内容自动化运行报告 {report['ran_at_display']}",
        "",
        f"- 热点是否变化：{'是' if report['content_changed'] else '否'}",
        f"- 变更签名：{report['new_signature'] or '无'}",
        f"- Gemini 是否执行：{'是' if report['gemini_ran'] else '否'}",
        f"- Gemini 审校是否执行：{'是' if report['review_ran'] else '否'}",
        f"- 规则质检是否执行：{'是' if report['audit_ran'] else '否'}",
        f"- Gemini 内容包是否匹配本轮热点：{'是' if report['fresh_bundle_ready'] else '否'}",
        f"- Buffer 是否执行：{'是' if report['distribution_ran'] else '否'}",
        "",
        "## 本轮热点标题",
    ]
    if report["new_titles"]:
        lines.extend(f"- {title}" for title in report["new_titles"])
    else:
        lines.append("- 当前没有可用热点标题。")

    if report["added_titles"]:
        lines.extend(["", "## 新增标题"])
        lines.extend(f"- {title}" for title in report["added_titles"])

    lines.extend(["", "## 脚本结果"])
    for step in report["steps"]:
        lines.append(
            f"- {step['script']} | {'ok' if step['ok'] else 'failed'} | {step['output'] or '无输出'}"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    load_env_files()
    timezone = ZoneInfo(os.getenv("PIPELINE_TIMEZONE", "Asia/Shanghai"))
    now = datetime.now(timezone)
    previous_payload = read_json(DATA_PATH)
    previous_signature = build_snapshot_signature(previous_payload)
    previous_titles = summarize_titles(previous_payload)

    steps: list[dict[str, Any]] = []
    updater_step = run_step("update_hot_news.py")
    steps.append(updater_step)
    if not updater_step["ok"]:
        raise SystemExit(updater_step["output"] or "update_hot_news.py failed")

    current_payload = read_json(DATA_PATH)
    new_signature = build_snapshot_signature(current_payload)
    new_titles = summarize_titles(current_payload)
    added_titles = [title for title in new_titles if title not in previous_titles]

    pipeline_state = read_json(PIPELINE_STATE_PATH) or {}
    last_success_signature = str(pipeline_state.get("last_success_signature", ""))
    content_changed = bool(new_signature and new_signature != last_success_signature)

    gemini_ran = False
    review_ran = False
    audit_ran = False
    fresh_bundle_ready = False
    distribution_ran = False
    if content_changed:
        gemini_step = run_step("generate_daily_content.py")
        steps.append(gemini_step)
        gemini_ran = True

        if gemini_step["ok"]:
            review_step = run_step("review_daily_content.py")
            steps.append(review_step)
            review_ran = True
        else:
            review_step = None

        bundle_payload = read_json(GEMINI_BUNDLE_PATH)
        fresh_bundle_ready = build_bundle_signature(bundle_payload) == new_signature and bool(new_signature)

        if gemini_step["ok"] and review_step and review_step["ok"] and fresh_bundle_ready:
            audit_step = run_step("audit_daily_content.py")
            steps.append(audit_step)
            audit_ran = True
        else:
            audit_step = None

        if (
            gemini_step["ok"]
            and review_step
            and review_step["ok"]
            and audit_step
            and audit_step["ok"]
            and fresh_bundle_ready
        ):
            distribution_step = run_step("distribute_daily_content.py")
            steps.append(distribution_step)
            distribution_ran = True
        else:
            distribution_step = None
    else:
        review_step = None
        audit_step = None
        distribution_step = None

    report = {
        "ran_at": now.isoformat(),
        "ran_at_display": f"{now.year}年{now.month}月{now.day}日 {now:%H:%M}",
        "previous_signature": previous_signature,
        "new_signature": new_signature,
        "content_changed": content_changed,
        "gemini_ran": gemini_ran,
        "review_ran": review_ran,
        "audit_ran": audit_ran,
        "fresh_bundle_ready": fresh_bundle_ready,
        "distribution_ran": distribution_ran,
        "new_titles": new_titles,
        "added_titles": added_titles,
        "steps": steps,
    }

    if content_changed and fresh_bundle_ready and all(step["ok"] for step in steps):
        pipeline_state["last_success_signature"] = new_signature
        pipeline_state["last_success_run_at"] = now.isoformat()
        pipeline_state["last_titles"] = new_titles
        write_json(PIPELINE_STATE_PATH, pipeline_state)

    write_json(PIPELINE_REPORT_JSON_PATH, report)
    PIPELINE_REPORT_MD_PATH.write_text(render_report(report), encoding="utf-8")

    if not all(step["ok"] for step in steps):
        raise SystemExit("pipeline finished with failures")

    if content_changed and fresh_bundle_ready:
        print("pipeline completed: content changed and distribution pipeline executed")
    elif content_changed:
        print("pipeline completed: content changed but no fresh Gemini bundle was available")
    else:
        print("pipeline completed: no meaningful content changes, skipped Gemini and Buffer")


if __name__ == "__main__":
    main()
