#!/usr/bin/env python3
"""
SEO/GEO automation runner.

This script performs a deterministic daily audit for crawlability, entity
grounding, structured data, citation readiness, and freshness signals. It does
not call external APIs, so it is safe to run from GitHub Actions or cron.
"""

from __future__ import annotations

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
GENERATED_DIR = ROOT / "generated"
REPORT_JSON_PATH = GENERATED_DIR / "seo-geo-report.json"
REPORT_MD_PATH = GENERATED_DIR / "seo-geo-report.md"
SITE_URL = "https://wenxingai.top"
TIMEZONE = ZoneInfo(os.getenv("PIPELINE_TIMEZONE", "Asia/Shanghai"))


CORE_PAGES = [
    {
        "path": "index.html",
        "url": f"{SITE_URL}/",
        "type": "homepage",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "facts/wenxing-ai.html",
        "url": f"{SITE_URL}/facts/wenxing-ai.html",
        "type": "grounding-page",
        "requires_json_ld": True,
        "requires_dl": True,
        "requires_verified": True,
    },
    {
        "path": "articles/index.html",
        "url": f"{SITE_URL}/articles/",
        "type": "article-hub",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "topics/index.html",
        "url": f"{SITE_URL}/topics/",
        "type": "topic-hub",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "geo-answers.html",
        "url": f"{SITE_URL}/geo-answers.html",
        "type": "answer-page",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "glossary.html",
        "url": f"{SITE_URL}/glossary.html",
        "type": "term-page",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "mingli-xuanxue-news.html",
        "url": f"{SITE_URL}/mingli-xuanxue-news.html",
        "type": "freshness-page",
        "requires_json_ld": True,
        "requires_modified_time": True,
    },
    {
        "path": "24jieqi/index.html",
        "url": f"{SITE_URL}/24jieqi/",
        "type": "hub-page",
        "requires_json_ld": True,
    },
]

REQUIRED_ROBOTS_TOKENS = [
    "Sitemap:",
    "AI-Policy:",
    "LLMs:",
    "GPTBot",
    "ClaudeBot",
    "PerplexityBot",
    "Google-Extended",
    "Bingbot",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def meta_content(html: str, name: str) -> str:
    pattern = re.compile(
        rf'<meta\s+(?:name|property)="{re.escape(name)}"\s+content="([^"]*)"',
        flags=re.IGNORECASE,
    )
    match = pattern.search(html)
    return match.group(1).strip() if match else ""


def canonical_href(html: str) -> str:
    match = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', html, flags=re.IGNORECASE)
    return match.group(1).strip() if match else ""


def page_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


def parse_json_ld_blocks(html: str) -> tuple[int, list[str]]:
    blocks = re.findall(
        r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    errors: list[str] = []
    for block in blocks:
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as exc:
            errors.append(str(exc))
    return len(blocks), errors


def add_issue(issues: list[dict[str, str]], severity: str, area: str, message: str) -> None:
    issues.append({"severity": severity, "area": area, "message": message})


def audit_page(page: dict[str, Any]) -> dict[str, Any]:
    relative_path = page["path"]
    full_path = ROOT / relative_path
    result: dict[str, Any] = {
        "path": relative_path,
        "url": page["url"],
        "type": page["type"],
        "status": "ok",
        "checks": {},
        "issues": [],
    }
    issues: list[dict[str, str]] = result["issues"]

    if not full_path.exists():
        add_issue(issues, "fail", "page", "page file is missing")
        result["status"] = "fail"
        return result

    html = full_path.read_text(encoding="utf-8")
    title = page_title(html)
    description = meta_content(html, "description")
    robots = meta_content(html, "robots")
    canonical = canonical_href(html)
    json_ld_count, json_ld_errors = parse_json_ld_blocks(html)

    result["checks"] = {
        "title_length": len(title),
        "description_length": len(description),
        "canonical": canonical,
        "robots": robots,
        "json_ld_blocks": json_ld_count,
    }

    if not title:
        add_issue(issues, "fail", "metadata", "missing <title>")
    if not description:
        add_issue(issues, "fail", "metadata", "missing meta description")
    elif len(description) < 40 or len(description) > 180:
        add_issue(issues, "warn", "metadata", "meta description should stay near 40-180 characters")
    if canonical != page["url"]:
        add_issue(issues, "fail", "canonical", f"canonical mismatch: {canonical or 'missing'}")
    if robots and "noindex" in robots.lower():
        add_issue(issues, "fail", "indexing", "robots meta contains noindex")
    if page.get("requires_json_ld") and json_ld_count == 0:
        add_issue(issues, "fail", "structured-data", "missing JSON-LD")
    for error in json_ld_errors:
        add_issue(issues, "fail", "structured-data", f"invalid JSON-LD: {error}")
    if page.get("requires_modified_time") and 'name="article:modified_time"' not in html:
        add_issue(issues, "warn", "freshness", "missing article:modified_time meta")
    if page.get("requires_dl") and "<dl" not in html:
        add_issue(issues, "fail", "grounding", "grounding page should expose facts in <dl>")
    if page.get("requires_verified") and "<dt>Verified</dt>" not in html:
        add_issue(issues, "fail", "grounding", "grounding page is missing Verified fact")

    severities = {issue["severity"] for issue in issues}
    result["status"] = "fail" if "fail" in severities else "warn" if "warn" in severities else "ok"
    return result


def build_page_inventory() -> list[dict[str, Any]]:
    pages = list(CORE_PAGES)
    known_paths = {page["path"] for page in pages}
    for folder, page_type in (("articles", "article-page"), ("topics", "topic-page")):
        directory = ROOT / folder
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.html")):
            relative_path = path.relative_to(ROOT).as_posix()
            if relative_path in known_paths:
                continue
            pages.append(
                {
                    "path": relative_path,
                    "url": f"{SITE_URL}/{relative_path}",
                    "type": page_type,
                    "requires_json_ld": True,
                    "requires_modified_time": True,
                }
            )
            known_paths.add(relative_path)
    return pages


def sitemap_urls() -> tuple[set[str], list[str]]:
    sitemap_path = ROOT / "sitemap.xml"
    if not sitemap_path.exists():
        return set(), ["sitemap.xml is missing"]
    try:
        tree = ET.parse(sitemap_path)
    except ET.ParseError as exc:
        return set(), [f"sitemap.xml parse error: {exc}"]
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = {
        loc.text.strip()
        for loc in tree.findall(f".//{namespace}loc")
        if loc.text and loc.text.strip()
    }
    return urls, []


def audit_infrastructure() -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    sitemap_entries, sitemap_errors = sitemap_urls()
    for error in sitemap_errors:
        add_issue(issues, "fail", "sitemap", error)

    try:
        robots = read_text("robots.txt")
    except FileNotFoundError:
        robots = ""
        add_issue(issues, "fail", "robots", "robots.txt is missing")
    for token in REQUIRED_ROBOTS_TOKENS:
        if token not in robots:
            add_issue(issues, "warn", "robots", f"robots.txt missing token: {token}")

    for page in CORE_PAGES:
        if page["url"] not in sitemap_entries:
            add_issue(issues, "warn", "sitemap", f"missing sitemap URL: {page['url']}")

    for relative_path, required_terms in {
        "llms.txt": ["问星AI", "facts/wenxing-ai.html", "引用指南"],
        "llms-full.txt": ["问星AI", "facts/wenxing-ai.html", "LLMS_HOT_TOPICS_START"],
        ".well-known/ai.txt": ["AI-Crawling: allowed", "facts/wenxing-ai.html"],
    }.items():
        path = ROOT / relative_path
        if not path.exists():
            add_issue(issues, "fail", "ai-docs", f"{relative_path} is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                add_issue(issues, "warn", "ai-docs", f"{relative_path} missing: {term}")

    severities = {issue["severity"] for issue in issues}
    return {
        "status": "fail" if "fail" in severities else "warn" if "warn" in severities else "ok",
        "sitemap_url_count": len(sitemap_entries),
        "issues": issues,
    }


def audit_content_pipeline() -> dict[str, Any]:
    checks: dict[str, Any] = {}
    issues: list[dict[str, str]] = []
    paths = {
        "hot_news": ROOT / "hot-news-data.json",
        "pipeline_report": ROOT / "generated" / "pipeline-report.json",
        "articles_index": ROOT / "generated" / "articles-index.json",
        "public_articles_index": ROOT / "articles" / "index.json",
        "public_articles_page": ROOT / "articles" / "index.html",
        "articles_report": ROOT / "generated" / "articles-report.md",
        "content_plan": ROOT / "generated" / "seo-geo-content-plan.md",
        "keyword_map": ROOT / "seo_geo_keywords.json",
    }

    for name, path in paths.items():
        checks[name] = path.exists()
        if not path.exists() and name in {"hot_news", "pipeline_report"}:
            add_issue(issues, "warn", "pipeline", f"{path.relative_to(ROOT)} is missing")

    if paths["hot_news"].exists():
        try:
            hot_news = json.loads(paths["hot_news"].read_text(encoding="utf-8"))
            checks["hot_news_items"] = len(hot_news.get("items") or [])
            checks["hot_news_updated_at"] = hot_news.get("updated_at", "")
        except json.JSONDecodeError as exc:
            add_issue(issues, "fail", "pipeline", f"hot-news-data.json parse error: {exc}")

    severities = {issue["severity"] for issue in issues}
    return {
        "status": "fail" if "fail" in severities else "warn" if "warn" in severities else "ok",
        "checks": checks,
        "issues": issues,
    }


def build_recommendations(page_results: list[dict[str, Any]], infrastructure: dict[str, Any]) -> list[str]:
    recommendations = [
        "保持 generate_seo_geo_topic_pages.py 每日运行，让 /topics/ 持续覆盖 AI命理、紫微斗数AI、八字、六爻、合盘、节气命理和玄学热点主题。",
        "保持内容流水线在热点变化时自动生成 /articles/ 深度文章，并自动写入 sitemap。",
        "配置 INDEXNOW_KEY 后，submit_indexnow.py 会自动向 IndexNow 提交 sitemap URL，减少新页面被发现的等待时间。",
    ]
    if infrastructure["status"] != "ok":
        recommendations.insert(0, "自动化基础设施出现缺项：先修 robots、sitemap、llms 或 AI policy，保证 AI 爬虫和搜索引擎能稳定发现权威页面。")
    if any(page["status"] == "fail" for page in page_results):
        recommendations.insert(0, "自动化审计发现失败页面：优先修复 canonical、JSON-LD、meta description 或实体事实块。")
    return recommendations


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# SEO/GEO 自动化健康报告 {report['ran_at_display']}",
        "",
        f"- 总体状态：{report['overall_status']}",
        f"- 页面检查：ok={report['summary']['pages_ok']} / warn={report['summary']['pages_warn']} / fail={report['summary']['pages_fail']}",
        f"- Sitemap URL 数：{report['infrastructure']['sitemap_url_count']}",
        "",
        "## 页面矩阵",
        "",
        "| 页面 | 类型 | 状态 | 关键问题 |",
        "|---|---|---|---|",
    ]
    for page in report["pages"]:
        issues = "; ".join(issue["message"] for issue in page["issues"][:3]) or "无"
        lines.append(f"| {page['path']} | {page['type']} | {page['status']} | {issues} |")

    lines.extend(["", "## 基础设施问题"])
    if report["infrastructure"]["issues"]:
        lines.extend(f"- [{issue['severity']}] {issue['area']}: {issue['message']}" for issue in report["infrastructure"]["issues"])
    else:
        lines.append("- 无")

    lines.extend(["", "## 内容流水线问题"])
    if report["content_pipeline"]["issues"]:
        lines.extend(f"- [{issue['severity']}] {issue['area']}: {issue['message']}" for issue in report["content_pipeline"]["issues"])
    else:
        lines.append("- 无")

    lines.extend(["", "## 下一步建议"])
    lines.extend(f"- {item}" for item in report["recommendations"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    now = datetime.now(TIMEZONE)
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    page_inventory = build_page_inventory()
    page_results = [audit_page(page) for page in page_inventory]
    infrastructure = audit_infrastructure()
    content_pipeline = audit_content_pipeline()

    pages_ok = sum(1 for page in page_results if page["status"] == "ok")
    pages_warn = sum(1 for page in page_results if page["status"] == "warn")
    pages_fail = sum(1 for page in page_results if page["status"] == "fail")
    has_failure = pages_fail > 0 or infrastructure["status"] == "fail" or content_pipeline["status"] == "fail"
    has_warning = pages_warn > 0 or infrastructure["status"] == "warn" or content_pipeline["status"] == "warn"
    overall_status = "fail" if has_failure else "warn" if has_warning else "ok"

    report = {
        "ran_at": now.isoformat(),
        "ran_at_display": now.strftime("%Y-%m-%d %H:%M %Z"),
        "overall_status": overall_status,
        "summary": {
            "pages_ok": pages_ok,
            "pages_warn": pages_warn,
            "pages_fail": pages_fail,
        },
        "pages": page_results,
        "infrastructure": infrastructure,
        "content_pipeline": content_pipeline,
        "recommendations": build_recommendations(page_results, infrastructure),
    }

    REPORT_JSON_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    REPORT_MD_PATH.write_text(render_markdown(report), encoding="utf-8")
    print(f"SEO/GEO report written to {REPORT_MD_PATH.relative_to(ROOT)} ({overall_status})")

    if has_failure and os.getenv("SEO_GEO_FAIL_ON_ERROR", "").strip().lower() in {"1", "true", "yes"}:
        sys.exit(1)


if __name__ == "__main__":
    main()