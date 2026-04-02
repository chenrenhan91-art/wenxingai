#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import re
import socket
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parent.parent
PROMPT_PATH = ROOT / "prompts" / "gemini_content_review_prompt.txt"
OUTPUT_DIR = ROOT / "generated"
BUNDLE_PATH = OUTPUT_DIR / "gemini-content-bundle.json"
MARKDOWN_OUTPUT_PATH = OUTPUT_DIR / "gemini-content-package.md"
REVIEW_REPORT_JSON_PATH = OUTPUT_DIR / "gemini-review-report.json"
REVIEW_REPORT_MD_PATH = OUTPUT_DIR / "gemini-review-report.md"
DEFAULT_MODEL = "gemini-2.5-pro"
DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_RETRY_ATTEMPTS = 3
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0 Safari/537.36"
)


def build_locale_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "site_article": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "seo_title": {"type": "string"},
                    "seo_description": {"type": "string"},
                    "excerpt": {"type": "string"},
                    "body_markdown": {"type": "string"},
                    "cta": {"type": "string"},
                },
                "required": [
                    "title",
                    "seo_title",
                    "seo_description",
                    "excerpt",
                    "body_markdown",
                    "cta",
                ],
            },
            "social_posts": {
                "type": "object",
                "properties": {
                    "threads": {"type": "array", "items": {"type": "string"}},
                    "x": {"type": "array", "items": {"type": "string"}},
                    "instagram": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["threads", "x", "instagram"],
            },
            "video_script": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "hook": {"type": "string"},
                    "script": {"type": "string"},
                    "cta": {"type": "string"},
                },
                "required": ["title", "hook", "script", "cta"],
            },
            "distribution_plan": {
                "type": "object",
                "properties": {
                    "threads": {"type": "string"},
                    "x": {"type": "string"},
                    "instagram": {"type": "string"},
                    "notes": {"type": "string"},
                },
                "required": ["threads", "x", "instagram", "notes"],
            },
        },
        "required": ["site_article", "social_posts", "video_script", "distribution_plan"],
    }


CONTENT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "campaign_summary": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "angle": {"type": "string"},
                "primary_cta": {"type": "string"},
            },
            "required": ["topic", "angle", "primary_cta"],
        },
        "localizations": {
            "type": "object",
            "properties": {
                "zh_cn": build_locale_schema(),
                "zh_hant": build_locale_schema(),
            },
            "required": ["zh_cn", "zh_hant"],
        },
    },
    "required": ["campaign_summary", "localizations"],
}


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


def strip_code_fences(value: str) -> str:
    text = value.strip()
    fenced = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.S)
    if fenced:
        return fenced.group(1).strip()
    return text


def require_string(payload: dict[str, Any], key: str, context: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"invalid Gemini review response: missing {context}.{key}")
    return value.strip()


def require_string_list(payload: dict[str, Any], key: str, context: str) -> list[str]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise RuntimeError(f"invalid Gemini review response: missing {context}.{key}")
    result = [item.strip() for item in value if isinstance(item, str) and item.strip()]
    if not result:
        raise RuntimeError(f"invalid Gemini review response: empty {context}.{key}")
    return result


def load_bundle() -> dict[str, Any]:
    if not BUNDLE_PATH.exists():
        raise RuntimeError("missing generated/gemini-content-bundle.json")
    return json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))


def build_prompt(bundle: dict[str, Any]) -> str:
    template = PROMPT_PATH.read_text(encoding="utf-8")
    return template.format(
        items_json=json.dumps(bundle.get("input_items") or [], ensure_ascii=False, indent=2),
        bundle_json=json.dumps(
            {
                "campaign_summary": bundle.get("campaign_summary", {}),
                "localizations": bundle.get("localizations", {}),
            },
            ensure_ascii=False,
            indent=2,
        ),
    )


def call_gemini(prompt: str, api_key: str, model: str) -> dict[str, Any]:
    endpoint = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{urllib.parse.quote(model, safe='')}:generateContent"
    )
    request_payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": CONTENT_SCHEMA,
        },
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(request_payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "x-goog-api-key": api_key,
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    timeout_seconds = int(
        os.getenv("GEMINI_TIMEOUT_SECONDS", str(DEFAULT_TIMEOUT_SECONDS)) or DEFAULT_TIMEOUT_SECONDS
    )
    last_exc: Exception | None = None
    for attempt in range(1, DEFAULT_RETRY_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, socket.timeout, TimeoutError) as exc:
            last_exc = exc
            if attempt >= DEFAULT_RETRY_ATTEMPTS:
                break
            time.sleep(min(2 * attempt, 6))
    assert last_exc is not None
    raise last_exc


def extract_candidate_text(response_payload: dict[str, Any]) -> str:
    texts: list[str] = []
    for candidate in response_payload.get("candidates", []):
        content = candidate.get("content") or {}
        for part in content.get("parts", []):
            text = part.get("text")
            if isinstance(text, str) and text.strip():
                texts.append(text.strip())
    if not texts:
        raise RuntimeError("Gemini review returned no text candidates")
    return "\n".join(texts).strip()


def validate_locale_content(locale_key: str, payload: dict[str, Any]) -> dict[str, Any]:
    site_article = payload.get("site_article")
    social_posts = payload.get("social_posts")
    video_script = payload.get("video_script")
    distribution_plan = payload.get("distribution_plan")
    if not isinstance(site_article, dict):
        raise RuntimeError(f"invalid review response: missing {locale_key}.site_article")
    if not isinstance(social_posts, dict):
        raise RuntimeError(f"invalid review response: missing {locale_key}.social_posts")
    if not isinstance(video_script, dict):
        raise RuntimeError(f"invalid review response: missing {locale_key}.video_script")
    if not isinstance(distribution_plan, dict):
        raise RuntimeError(f"invalid review response: missing {locale_key}.distribution_plan")

    return {
        "site_article": {
            "title": require_string(site_article, "title", f"{locale_key}.site_article"),
            "seo_title": require_string(site_article, "seo_title", f"{locale_key}.site_article"),
            "seo_description": require_string(
                site_article,
                "seo_description",
                f"{locale_key}.site_article",
            ),
            "excerpt": require_string(site_article, "excerpt", f"{locale_key}.site_article"),
            "body_markdown": require_string(
                site_article,
                "body_markdown",
                f"{locale_key}.site_article",
            ),
            "cta": require_string(site_article, "cta", f"{locale_key}.site_article"),
        },
        "social_posts": {
            "threads": require_string_list(social_posts, "threads", f"{locale_key}.social_posts"),
            "x": require_string_list(social_posts, "x", f"{locale_key}.social_posts"),
            "instagram": require_string_list(
                social_posts,
                "instagram",
                f"{locale_key}.social_posts",
            ),
        },
        "video_script": {
            "title": require_string(video_script, "title", f"{locale_key}.video_script"),
            "hook": require_string(video_script, "hook", f"{locale_key}.video_script"),
            "script": require_string(video_script, "script", f"{locale_key}.video_script"),
            "cta": require_string(video_script, "cta", f"{locale_key}.video_script"),
        },
        "distribution_plan": {
            "threads": require_string(
                distribution_plan,
                "threads",
                f"{locale_key}.distribution_plan",
            ),
            "x": require_string(distribution_plan, "x", f"{locale_key}.distribution_plan"),
            "instagram": require_string(
                distribution_plan,
                "instagram",
                f"{locale_key}.distribution_plan",
            ),
            "notes": require_string(
                distribution_plan,
                "notes",
                f"{locale_key}.distribution_plan",
            ),
        },
    }


def validate_reviewed_content(content: dict[str, Any]) -> dict[str, Any]:
    campaign_summary = content.get("campaign_summary")
    localizations = content.get("localizations")
    if not isinstance(campaign_summary, dict):
        raise RuntimeError("invalid review response: missing campaign_summary")
    if not isinstance(localizations, dict):
        raise RuntimeError("invalid review response: missing localizations")

    return {
        "campaign_summary": {
            "topic": require_string(campaign_summary, "topic", "campaign_summary"),
            "angle": require_string(campaign_summary, "angle", "campaign_summary"),
            "primary_cta": require_string(
                campaign_summary,
                "primary_cta",
                "campaign_summary",
            ),
        },
        "localizations": {
            "zh_cn": validate_locale_content("zh_cn", localizations.get("zh_cn") or {}),
            "zh_hant": validate_locale_content("zh_hant", localizations.get("zh_hant") or {}),
        },
    }


def render_markdown(bundle: dict[str, Any]) -> str:
    def render_locale_section(locale_key: str, locale_content: dict[str, Any]) -> list[str]:
        locale_label = "简体中文" if locale_key == "zh_cn" else "繁體中文"
        article = locale_content["site_article"]
        social = locale_content["social_posts"]
        video = locale_content["video_script"]
        plan = locale_content["distribution_plan"]

        lines = [
            f"## {locale_label}",
            "",
            "### 网站文章",
            f"- 标题：{article['title']}",
            f"- SEO 标题：{article['seo_title']}",
            f"- SEO 描述：{article['seo_description']}",
            f"- 摘要：{article['excerpt']}",
            f"- CTA：{article['cta']}",
            "",
            article["body_markdown"],
            "",
            "### Threads 文案",
        ]
        lines.extend(f"{index}. {post}" for index, post in enumerate(social["threads"], start=1))
        lines.extend(["", "### X 文案"])
        lines.extend(f"{index}. {post}" for index, post in enumerate(social["x"], start=1))
        lines.extend(["", "### Instagram 文案"])
        lines.extend(
            f"{index}. {post}" for index, post in enumerate(social["instagram"], start=1)
        )
        lines.extend(
            [
                "",
                "### 短视频脚本",
                f"- 标题：{video['title']}",
                f"- Hook：{video['hook']}",
                f"- CTA：{video['cta']}",
                "",
                video["script"],
                "",
                "### 建议排期",
                f"- Threads：{plan['threads']}",
                f"- X：{plan['x']}",
                f"- Instagram：{plan['instagram']}",
                f"- 备注：{plan['notes']}",
                "",
            ]
        )
        return lines

    lines = [
        f"# 问星AI 每日内容包 {bundle['source_snapshot_updated_at']}",
        "",
        f"- 生成时间：{bundle['generated_at_display']}",
        f"- 生成模型：{bundle['model']}",
        f"- 审校模型：{bundle.get('review_model', '')}",
        f"- 建议文章 slug：{bundle['slug']}",
        f"- 今日主题：{bundle['campaign_summary']['topic']}",
        f"- 今日切入角度：{bundle['campaign_summary']['angle']}",
        f"- 今日主 CTA：{bundle['campaign_summary']['primary_cta']}",
        "",
    ]
    for locale_key in ("zh_cn", "zh_hant"):
        lines.extend(render_locale_section(locale_key, bundle["localizations"][locale_key]))
    lines.extend(["## 输入来源"])
    for index, item in enumerate(bundle["input_items"], start=1):
        lines.append(
            f"{index}. {item['title']} | {item['source']} | {item['published']} | {item['url']}"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    load_env_files()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Gemini review failed: missing GEMINI_API_KEY")

    model = os.getenv("GEMINI_REVIEW_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    try:
        bundle = load_bundle()
        prompt = build_prompt(bundle)
        response_payload = call_gemini(prompt, api_key, model)
        candidate_text = extract_candidate_text(response_payload)
        reviewed_content = validate_reviewed_content(json.loads(strip_code_fences(candidate_text)))

        bundle["campaign_summary"] = reviewed_content["campaign_summary"]
        bundle["localizations"] = reviewed_content["localizations"]
        bundle["review_model"] = model
        bundle["reviewed_at"] = bundle.get("generated_at")

        BUNDLE_PATH.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
        MARKDOWN_OUTPUT_PATH.write_text(render_markdown(bundle), encoding="utf-8")

        report = {
            "review_model": model,
            "source_snapshot_updated_at": bundle.get("source_snapshot_updated_at", ""),
            "status": "reviewed",
        }
        REVIEW_REPORT_JSON_PATH.write_text(
            json.dumps(report, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        REVIEW_REPORT_MD_PATH.write_text(
            "\n".join(
                [
                    f"# 问星AI 内容审校报告 {bundle.get('source_snapshot_updated_at', '')}",
                    "",
                    f"- 审校状态：{report['status']}",
                    f"- 审校模型：{report['review_model']}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        print(f"reviewed Gemini content bundle using {model}")
    except (HTTPError, URLError, socket.timeout, TimeoutError) as exc:
        raise SystemExit(f"Gemini review failed: network or API error: {exc}")
    except Exception as exc:
        raise SystemExit(f"Gemini review failed: {exc}")


if __name__ == "__main__":
    main()
