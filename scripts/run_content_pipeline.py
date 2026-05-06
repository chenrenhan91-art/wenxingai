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


def env_flag(name: str, default: bool = False) -> bool:
    value = os.getenv(name, "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "on"}


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
        f"- 总体状态：{report['overall_status']}",
        f"- 本轮是否强制刷新：{'是' if report['force_refresh'] else '否'}",
        f"- 热点是否变化：{'是' if report['content_changed'] else '否'}",
        f"- 变更签名：{report['new_signature'] or '无'}",
        f"- Gemini 是否执行：{'是' if report['gemini_ran'] else '否'}",
        f"- Gemini 审校是否执行：{'是' if report['review_ran'] else '否'}",
        f"- 规则质检是否执行：{'是' if report['audit_ran'] else '否'}",
        f"- Gemini 内容包是否匹配本轮热点：{'是' if report['fresh_bundle_ready'] else '否'}",
        f"- Buffer 是否执行：{'是' if report['distribution_ran'] else '否'}",
        f"- 深度文章是否生成：{'是' if report['articles_ran'] else '否'}",
        f"- 阶段状态：抓取={report['stage_status'].get('update')}, 生成={report['stage_status'].get('generate')}, 审校={report['stage_status'].get('review')}, 质检={report['stage_status'].get('audit')}, 分发={report['stage_status'].get('distribution')}, 文章={report['stage_status'].get('articles')}",
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

    if report.get("ops_hints"):
        lines.extend(["", "## 次日运营建议"])
        lines.extend(f"- {hint}" for hint in report["ops_hints"])

    if report["failed_scripts"]:
        lines.extend(["", "## 失败脚本"])
        lines.extend(f"- {title}" for title in report["failed_scripts"])

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
    force_refresh = env_flag("PIPELINE_FORCE_REFRESH")
    now = datetime.now(timezone)
    previous_payload = read_json(DATA_PATH)
    previous_signature = build_snapshot_signature(previous_payload)
    previous_titles = summarize_titles(previous_payload)

    steps: list[dict[str, Any]] = []
    stage_status = {
        "update": "skipped",
        "generate": "skipped",
        "review": "skipped",
        "audit": "skipped",
        "distribution": "skipped",
        "articles": "skipped",
    }
    updater_step = run_step("update_hot_news.py")
    steps.append(updater_step)
    stage_status["update"] = "ok" if updater_step["ok"] else "failed"

    current_payload = read_json(DATA_PATH)
    new_signature = build_snapshot_signature(current_payload)
    new_titles = summarize_titles(current_payload)
    added_titles = [title for title in new_titles if title not in previous_titles]
    ops_hints = [str(hint).strip() for hint in (current_payload or {}).get("ops_hints") or [] if str(hint).strip()]

    pipeline_state = read_json(PIPELINE_STATE_PATH) or {}
    last_success_signature = str(pipeline_state.get("last_success_signature", ""))
    content_changed = bool(new_signature and new_signature != last_success_signature)
    should_refresh_content = bool(new_signature) and (content_changed or force_refresh)

    gemini_ran = False
    review_ran = False
    audit_ran = False
    fresh_bundle_ready = False
    distribution_ran = False
    articles_ran = False
    if should_refresh_content:
        gemini_step = run_step("generate_daily_content.py")
        steps.append(gemini_step)
        gemini_ran = True
        stage_status["generate"] = "ok" if gemini_step["ok"] else "failed"

        if gemini_step["ok"]:
            review_step = run_step("review_daily_content.py")
            steps.append(review_step)
            review_ran = True
            stage_status["review"] = "ok" if review_step["ok"] else "failed"
        else:
            review_step = None
            stage_status["review"] = "blocked"

        bundle_payload = read_json(GEMINI_BUNDLE_PATH)
        fresh_bundle_ready = build_bundle_signature(bundle_payload) == new_signature and bool(new_signature)

        if gemini_step["ok"] and review_step and review_step["ok"] and fresh_bundle_ready:
            audit_step = run_step("audit_daily_content.py")
            steps.append(audit_step)
            audit_ran = True
            stage_status["audit"] = "ok" if audit_step["ok"] else "failed"
        else:
            audit_step = None
            stage_status["audit"] = "blocked"

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
            stage_status["distribution"] = "ok" if distribution_step["ok"] else "failed"
            
            # 分发成功后，生成深度文章（可选但推荐）
            if distribution_step["ok"]:
                article_step = run_step("generate_article_from_snippets.py")
                steps.append(article_step)
                articles_ran = True
                stage_status["articles"] = "ok" if article_step["ok"] else "failed"
        else:
            distribution_step = None
            stage_status["distribution"] = "blocked"
    else:
        review_step = None
        audit_step = None
        distribution_step = None
        stage_status["generate"] = "skipped"
        stage_status["review"] = "skipped"
        stage_status["audit"] = "skipped"
        stage_status["distribution"] = "skipped"

    failed_steps = [step for step in steps if not step["ok"]]
    if not updater_step["ok"]:
        overall_status = "failed_update"
    elif stage_status["generate"] == "failed":
        overall_status = "failed_generate"
    elif stage_status["review"] == "failed":
        overall_status = "failed_review"
    elif stage_status["audit"] == "failed":
        overall_status = "failed_audit"
    elif stage_status["distribution"] == "failed":
        overall_status = "failed_distribution"
    elif failed_steps:
        overall_status = "partial_failure"
    else:
        overall_status = "success"

    report = {
        "ran_at": now.isoformat(),
        "ran_at_display": f"{now.year}年{now.month}月{now.day}日 {now:%H:%M}",
        "overall_status": overall_status,
        "force_refresh": force_refresh,
        "previous_signature": previous_signature,
        "new_signature": new_signature,
        "content_changed": content_changed,
        "gemini_ran": gemini_ran,
        "review_ran": review_ran,
        "audit_ran": audit_ran,
        "fresh_bundle_ready": fresh_bundle_ready,
        "distribution_ran": distribution_ran,
        "articles_ran": articles_ran,
        "stage_status": stage_status,
        "new_titles": new_titles,
        "added_titles": added_titles,
        "ops_hints": ops_hints,
        "failed_scripts": [step["script"] for step in failed_steps],
        "steps": steps,
    }

    if content_changed and fresh_bundle_ready and not failed_steps:
        pipeline_state["last_success_signature"] = new_signature
        pipeline_state["last_success_run_at"] = now.isoformat()
        pipeline_state["last_titles"] = new_titles
        write_json(PIPELINE_STATE_PATH, pipeline_state)

    write_json(PIPELINE_REPORT_JSON_PATH, report)
    PIPELINE_REPORT_MD_PATH.write_text(render_report(report), encoding="utf-8")

    if not updater_step["ok"]:
        raise SystemExit("pipeline failed during hot news update")

    if failed_steps:
        print(
            "pipeline completed with partial failures: "
            + ", ".join(step["script"] for step in failed_steps)
        )
    elif should_refresh_content and fresh_bundle_ready:
        if content_changed:
            print("pipeline completed: content changed and distribution pipeline executed")
        else:
            print("pipeline completed: forced refresh executed and distribution pipeline ran")
    elif should_refresh_content:
        if content_changed:
            print("pipeline completed: content changed but no fresh Gemini bundle was available")
        else:
            print("pipeline completed: forced refresh ran but no fresh Gemini bundle was available")
    else:
        print("pipeline completed: no meaningful content changes, skipped Gemini and Buffer")


if __name__ == "__main__":
    main()
