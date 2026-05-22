#!/usr/bin/env python3
"""Create a deterministic SEO/GEO content operations brief."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
KEYWORDS_PATH = ROOT / "seo_geo_keywords.json"
HOT_NEWS_PATH = ROOT / "hot-news-data.json"
ARTICLES_INDEX_PATH = ROOT / "articles" / "index.json"
OUTPUT_JSON_PATH = ROOT / "generated" / "seo-geo-content-plan.json"
OUTPUT_MD_PATH = ROOT / "generated" / "seo-geo-content-plan.md"
TIMEZONE = ZoneInfo("Asia/Shanghai")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def normalize_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def hot_news_context() -> dict[str, Any]:
    payload = load_json(HOT_NEWS_PATH, {})
    items = payload.get("items") or []
    titles = [str(item.get("title", "")).strip() for item in items if item.get("title")]
    keywords: list[str] = []
    categories: Counter[str] = Counter()
    for item in items:
        categories[str(item.get("category") or "趋势观察")] += 1
        keywords.extend(str(keyword) for keyword in item.get("matched_keywords") or [])
    return {
        "updated_at": payload.get("updated_at", ""),
        "titles": titles[:10],
        "keywords": Counter(keywords).most_common(20),
        "categories": categories.most_common(10),
        "search_text": normalize_text(" ".join(titles + keywords)),
    }


def existing_article_text() -> str:
    payload = load_json(ARTICLES_INDEX_PATH, {})
    articles = payload.get("articles") or []
    chunks: list[str] = []
    for article in articles:
        chunks.append(str(article.get("title", "")))
        chunks.append(str(article.get("seo_title", "")))
        chunks.extend(str(keyword) for keyword in article.get("keywords") or [])
    return normalize_text(" ".join(chunks))


def score_cluster(cluster: dict[str, Any], hot_text: str, article_text: str) -> dict[str, Any]:
    primary = [str(item) for item in cluster.get("primary_keywords") or []]
    secondary = [str(item) for item in cluster.get("secondary_keywords") or []]
    all_keywords = primary + secondary
    hot_matches = [keyword for keyword in all_keywords if normalize_text(keyword) in hot_text]
    article_matches = [keyword for keyword in primary if normalize_text(keyword) in article_text]
    missing_pages = [page for page in cluster.get("preferred_pages") or [] if not page_exists(str(page))]
    score = int(cluster.get("priority", 0)) + len(hot_matches) * 12 + len(missing_pages) * 5
    if not article_matches:
        score += 10
    return {
        "id": cluster.get("id"),
        "name": cluster.get("name"),
        "score": score,
        "priority": cluster.get("priority", 0),
        "hot_matches": hot_matches,
        "article_coverage": article_matches,
        "missing_pages": missing_pages,
        "primary_keywords": primary,
        "target_questions": cluster.get("target_questions") or [],
        "preferred_pages": cluster.get("preferred_pages") or [],
        "content_angles": cluster.get("content_angles") or [],
        "automation_cadence": cluster.get("automation_cadence", "weekly"),
    }


def page_exists(url_path: str) -> bool:
    if url_path == "/":
        return (ROOT / "index.html").exists()
    normalized = url_path.strip("/")
    if not normalized:
        return (ROOT / "index.html").exists()
    if normalized.endswith("/"):
        return (ROOT / normalized / "index.html").exists()
    return (ROOT / normalized.lstrip("/")).exists()


def build_briefs(scored_clusters: list[dict[str, Any]], hot: dict[str, Any]) -> list[dict[str, Any]]:
    briefs: list[dict[str, Any]] = []
    for cluster in scored_clusters[:5]:
        primary_keyword = cluster["primary_keywords"][0] if cluster["primary_keywords"] else cluster["name"]
        question = cluster["target_questions"][0] if cluster["target_questions"] else f"{primary_keyword}是什么？"
        angle = cluster["content_angles"][0] if cluster["content_angles"] else "补齐搜索意图与AI引用事实"
        action = "new_article" if "/articles/" in cluster["preferred_pages"] else "update_page"
        briefs.append(
            {
                "cluster_id": cluster["id"],
                "cluster_name": cluster["name"],
                "action": action,
                "primary_keyword": primary_keyword,
                "target_question": question,
                "suggested_title": f"{primary_keyword}怎么理解？问星AI的理性命理观察",
                "suggested_h2": [
                    f"{primary_keyword}的搜索意图是什么",
                    f"问星AI如何解释{primary_keyword}",
                    "传统命理与AI趋势分析的边界",
                    "可引用事实与常见问题",
                ],
                "internal_links": [
                    "/facts/wenxing-ai.html",
                    "/geo-answers.html",
                    "/glossary.html",
                    "/mingli-xuanxue-news.html",
                ],
                "hot_context": hot["titles"][:3],
                "angle": angle,
            }
        )
    return briefs


def render_markdown(plan: dict[str, Any]) -> str:
    lines = [
        f"# SEO/GEO 内容运营 Brief {plan['generated_at_display']}",
        "",
        f"- 热点数据日期：{plan['hot_news'].get('updated_at') or '未知'}",
        f"- 本轮推荐主题数：{len(plan['briefs'])}",
        "",
        "## 热点信号",
    ]
    if plan["hot_news"]["titles"]:
        lines.extend(f"- {title}" for title in plan["hot_news"]["titles"][:6])
    else:
        lines.append("- 暂无热点标题。")

    lines.extend(["", "## 优先主题评分"])
    for cluster in plan["scored_clusters"][:8]:
        matches = "、".join(cluster["hot_matches"]) or "无"
        coverage = "、".join(cluster["article_coverage"]) or "文章库未覆盖核心词"
        lines.append(f"- {cluster['name']}：score={cluster['score']}；热点匹配={matches}；覆盖={coverage}")

    lines.extend(["", "## 今日/本周内容动作"])
    for brief in plan["briefs"]:
        lines.extend(
            [
                f"### {brief['cluster_name']}",
                f"- 动作：{brief['action']}",
                f"- 主关键词：{brief['primary_keyword']}",
                f"- 目标问题：{brief['target_question']}",
                f"- 建议标题：{brief['suggested_title']}",
                f"- 角度：{brief['angle']}",
                f"- 内链：{', '.join(brief['internal_links'])}",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> None:
    now = datetime.now(TIMEZONE)
    config = load_json(KEYWORDS_PATH, {"clusters": []})
    hot = hot_news_context()
    article_text = existing_article_text()
    scored = [score_cluster(cluster, hot["search_text"], article_text) for cluster in config.get("clusters") or []]
    scored.sort(key=lambda item: item["score"], reverse=True)
    plan = {
        "generated_at": now.isoformat(),
        "generated_at_display": now.strftime("%Y-%m-%d %H:%M %Z"),
        "site_positioning": config.get("site_positioning", ""),
        "hot_news": {key: value for key, value in hot.items() if key != "search_text"},
        "scored_clusters": scored,
        "briefs": build_briefs(scored, hot),
        "monthly_ai_prompt_tests": config.get("monthly_ai_prompt_tests") or [],
    }
    OUTPUT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON_PATH.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    OUTPUT_MD_PATH.write_text(render_markdown(plan), encoding="utf-8")
    print(f"SEO/GEO content plan written to {OUTPUT_MD_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()