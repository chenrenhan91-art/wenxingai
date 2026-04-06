#!/usr/bin/env python3

from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "generated"
BUNDLE_PATH = OUTPUT_DIR / "gemini-content-bundle.json"
AUDIT_REPORT_JSON_PATH = OUTPUT_DIR / "gemini-audit-report.json"
AUDIT_REPORT_MD_PATH = OUTPUT_DIR / "gemini-audit-report.md"


def env_int(name: str, default: int) -> int:
    raw = (os.getenv(name) or "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return value if value >= 0 else default

FORBIDDEN_PHRASES = [
    "我无法确认",
    "作為AI",
    "作为AI",
    "身為AI",
    "身为AI",
    "語言模型",
    "语言模型",
    "绝对准确",
    "絕對準確",
    "一定会发生",
    "一定會發生",
    "注定",
    "命中注定",
    "柯文哲",
    "政治",
    "政党",
    "政黨",
    "宗教",
]

ZH_CN_TRADITIONAL_MARKERS = list("這為專們體點與應讓還該關說歡請個嗎將風夯盲")
ZH_HANT_SIMPLIFIED_MARKERS = list("这为专们体点与应让还该关说欢迎请个吗将风夯盲")


def load_bundle() -> dict:
    if not BUNDLE_PATH.exists():
        raise SystemExit("missing generated/gemini-content-bundle.json")
    return json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))


def count_markers(text: str, markers: list[str]) -> int:
    return sum(text.count(marker) for marker in markers)


def audit_locale(locale_key: str, payload: dict) -> tuple[list[str], list[str]]:
    warnings: list[str] = []
    blocking: list[str] = []
    social_posts = (payload.get("social_posts") or {})
    expected_counts = {
        "threads": env_int("SOCIAL_THREADS_POST_COUNT", 2),
        "x": env_int("SOCIAL_X_POST_COUNT", 2),
        "instagram": env_int("SOCIAL_INSTAGRAM_POST_COUNT", 2),
    }

    for platform in ("threads", "x", "instagram"):
        posts = social_posts.get(platform) or []
        expected = expected_counts.get(platform, 0)
        actual = len(posts)
        if actual != expected:
            blocking.append(
                f"{locale_key}.{platform} 文案数量不符合要求：当前 {actual}，期望 {expected}"
            )
        if not posts:
            continue
        for index, post in enumerate(posts, start=1):
            text = str(post).strip()
            if not text:
                blocking.append(f"{locale_key}.{platform} 第 {index} 条文案为空")
                continue
            for phrase in FORBIDDEN_PHRASES:
                if phrase in text:
                    blocking.append(f"{locale_key}.{platform} 第 {index} 条文案含模型措辞：{phrase}")
            if any(char in text for char in "🙂😂🤣🥲😊😅😍✨🌟🤔📌🔮"):
                blocking.append(f"{locale_key}.{platform} 第 {index} 条文案含 emoji")
            if platform == "x" and len(text) > 160:
                warnings.append(f"{locale_key}.x 第 {index} 条文案偏长：{len(text)} 字符")

            if locale_key == "zh_cn":
                traditional_count = count_markers(text, ZH_CN_TRADITIONAL_MARKERS)
                if traditional_count >= 6:
                    warnings.append(
                        f"{locale_key}.{platform} 第 {index} 条文案可能混入较多繁体字：{traditional_count}"
                    )
            if locale_key == "zh_hant":
                simplified_count = count_markers(text, ZH_HANT_SIMPLIFIED_MARKERS)
                if simplified_count >= 6:
                    warnings.append(
                        f"{locale_key}.{platform} 第 {index} 条文案可能混入较多简体字：{simplified_count}"
                    )

    article = (payload.get("site_article") or {})
    for field in ("title", "seo_title", "seo_description", "excerpt", "body_markdown", "cta"):
        if not str(article.get(field, "")).strip():
            blocking.append(f"{locale_key}.site_article.{field} 为空")

    article_text = " ".join(str(article.get(field, "")) for field in article)
    for phrase in FORBIDDEN_PHRASES:
        if phrase in article_text:
            blocking.append(f"{locale_key}.site_article 含模型措辞：{phrase}")

    return warnings, blocking


def main() -> None:
    bundle = load_bundle()
    localizations = bundle.get("localizations") or {}
    warnings: list[str] = []
    blocking: list[str] = []

    for locale_key in ("zh_cn", "zh_hant"):
        locale_payload = localizations.get(locale_key) or {}
        if not locale_payload:
            blocking.append(f"缺少语言版本：{locale_key}")
            continue
        locale_warnings, locale_blocking = audit_locale(locale_key, locale_payload)
        warnings.extend(locale_warnings)
        blocking.extend(locale_blocking)

    input_items = bundle.get("input_items") or []
    if isinstance(input_items, list) and input_items:
        source_group_counter = Counter(
            str(item.get("source_group", ""))
            for item in input_items
            if isinstance(item, dict) and item.get("source_group")
        )
        category_counter = Counter(
            str(item.get("category", ""))
            for item in input_items
            if isinstance(item, dict) and item.get("category")
        )

        distinct_source_groups = len(source_group_counter)
        distinct_categories = len(category_counter)
        if distinct_source_groups < 3:
            blocking.append(
                f"热点来源多样性不足：当前 source_group {distinct_source_groups} 类，至少需要 3 类"
            )
        if distinct_categories < 3:
            blocking.append(
                f"热点类别多样性不足：当前 category {distinct_categories} 类，至少需要 3 类"
            )

        if source_group_counter.get("community", 0) == 0:
            warnings.append("本轮缺少社区来源话题，可能影响互动率")
        if source_group_counter.get("news", 0) == 0:
            warnings.append("本轮缺少新闻来源话题，可能影响可信度")

    status = "passed" if not blocking else "failed"
    report = {
        "status": status,
        "warnings": warnings,
        "blocking_issues": blocking,
    }
    AUDIT_REPORT_JSON_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        f"# 问星AI 内容质检报告 {bundle.get('source_snapshot_updated_at', '')}",
        "",
        f"- 状态：{status}",
        "",
        "## 阻断问题",
    ]
    if blocking:
        lines.extend(f"- {item}" for item in blocking)
    else:
        lines.append("- 无")
    lines.extend(["", "## 提醒项"])
    if warnings:
        lines.extend(f"- {item}" for item in warnings)
    else:
        lines.append("- 无")
    lines.append("")
    AUDIT_REPORT_MD_PATH.write_text("\n".join(lines), encoding="utf-8")

    if blocking:
        raise SystemExit("content audit failed")
    print(f"content audit passed with {len(warnings)} warnings")


if __name__ == "__main__":
    main()
