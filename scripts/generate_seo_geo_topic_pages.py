#!/usr/bin/env python3
"""Generate public SEO/GEO topic pages from the keyword matrix."""

from __future__ import annotations

import json
import re
from datetime import datetime
from html import escape
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
KEYWORDS_PATH = ROOT / "seo_geo_keywords.json"
HOT_NEWS_PATH = ROOT / "hot-news-data.json"
TOPICS_DIR = ROOT / "topics"
TOPICS_INDEX_PATH = TOPICS_DIR / "index.html"
TOPICS_JSON_PATH = TOPICS_DIR / "index.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
TIMEZONE = ZoneInfo("Asia/Shanghai")
SITE_URL = "https://wenxingai.top"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def clean_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9-]+", "-", value.strip().lower())
    return re.sub(r"-+", "-", slug).strip("-") or "topic"


def hot_titles_for_cluster(cluster: dict[str, Any], hot_items: list[dict[str, Any]]) -> list[str]:
    keywords = [
        str(keyword).lower()
        for keyword in (cluster.get("primary_keywords") or []) + (cluster.get("secondary_keywords") or [])
    ]
    matches: list[str] = []
    fallback: list[str] = []
    for item in hot_items:
        title = str(item.get("title", "")).strip()
        if not title:
            continue
        fallback.append(title)
        haystack = " ".join(
            [
                title,
                str(item.get("category", "")),
                " ".join(str(keyword) for keyword in item.get("matched_keywords") or []),
            ]
        ).lower()
        if any(keyword and keyword in haystack for keyword in keywords):
            matches.append(title)
    return (matches or fallback)[:5]


def render_links(paths: list[str]) -> str:
    labels = {
        "/": "问星AI首页",
        "/facts/wenxing-ai.html": "问星AI实体事实页",
        "/geo-answers.html": "常见问题",
        "/glossary.html": "命理词典",
        "/mingli-xuanxue-news.html": "命理玄学热点资讯",
        "/articles/": "深度文章",
        "/24jieqi/": "二十四节气命理",
    }
    safe_paths = paths or ["/", "/facts/wenxing-ai.html", "/geo-answers.html", "/glossary.html"]
    return "".join(
        f'<a href="{escape(path, quote=True)}">{escape(labels.get(path, path))}</a>'
        for path in safe_paths
    )


def render_topic_page(cluster: dict[str, Any], hot_titles: list[str], today: str) -> str:
    topic_id = clean_slug(str(cluster.get("id", cluster.get("name", "topic"))))
    name = str(cluster.get("name", "SEO/GEO专题"))
    primary_keywords = [str(item) for item in cluster.get("primary_keywords") or []]
    secondary_keywords = [str(item) for item in cluster.get("secondary_keywords") or []]
    questions = [str(item) for item in cluster.get("target_questions") or []]
    angles = [str(item) for item in cluster.get("content_angles") or []]
    preferred_pages = [str(item) for item in cluster.get("preferred_pages") or []]
    canonical = f"{SITE_URL}/topics/{topic_id}.html"
    keyword_text = "、".join(primary_keywords[:4])
    description = f"问星AI{name}专题，围绕{keyword_text}等关键词，解释搜索意图、命理概念、AI命理边界与相关页面入口。"
    faq_items = [
        {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f"{question}可以从{name}的搜索意图、传统命理概念和AI辅助分析边界三个层面理解。问星AI将相关内容拆分为实体事实、FAQ、术语和深度文章，便于用户和AI检索系统交叉验证。",
            },
        }
        for question in questions[:6]
    ]
    json_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": canonical,
                    "url": canonical,
                    "name": f"问星AI{name}专题",
                    "description": description,
                    "dateModified": today,
                    "inLanguage": "zh-CN",
                    "isPartOf": {"@id": f"{SITE_URL}/#website"},
                    "about": {"@id": f"{SITE_URL}/facts/wenxing-ai.html#entity"},
                    "keywords": primary_keywords + secondary_keywords,
                },
                {
                    "@type": "FAQPage",
                    "@id": f"{canonical}#faq",
                    "mainEntity": faq_items,
                },
                {
                    "@type": "BreadcrumbList",
                    "@id": f"{canonical}#breadcrumb",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "首页", "item": f"{SITE_URL}/"},
                        {"@type": "ListItem", "position": 2, "name": "SEO/GEO专题", "item": f"{SITE_URL}/topics/"},
                        {"@type": "ListItem", "position": 3, "name": name, "item": canonical},
                    ],
                },
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
    primary_html = "".join(f"<span>{escape(keyword)}</span>" for keyword in primary_keywords)
    secondary_html = "".join(f"<span>{escape(keyword)}</span>" for keyword in secondary_keywords)
    questions_html = "".join(
        f"<details><summary>{escape(question)}</summary><p>{escape(question)}的核心不是寻找单一绝对答案，而是判断用户想了解概念定义、工具差异、使用边界还是行动参考。问星AI会通过实体事实页、FAQ、术语页和深度文章提供可交叉验证的信息。</p></details>"
        for question in questions[:6]
    )
    angles_html = "".join(f"<li>{escape(angle)}</li>" for angle in angles[:6])
    hot_html = "".join(f"<li>{escape(title)}</li>" for title in hot_titles[:5]) or "<li>暂无热点信号，等待下一轮自动抓取。</li>"
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>问星AI{name}专题 | {escape(keyword_text)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="ai-content-policy" content="indexable, summarizable, citable">
  <meta name="article:modified_time" content="{today}T00:00:00+08:00">
  <link rel="canonical" href="{canonical}">
  <style>
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Noto Sans SC","PingFang SC",sans-serif; line-height:1.75; color:#202637; background:#f7f7fb; }}
    header, main, footer {{ max-width:920px; margin:0 auto; padding:0 20px; }}
    header {{ padding-top:42px; padding-bottom:18px; }}
    nav {{ font-size:14px; color:#657186; margin-bottom:22px; }}
    a {{ color:#3656a7; text-decoration:none; }}
    h1 {{ margin:0 0 12px; font-size:34px; line-height:1.2; color:#101828; }}
    h2 {{ margin:34px 0 12px; font-size:22px; color:#101828; }}
    .lead {{ color:#526070; margin-bottom:24px; }}
    dl {{ display:grid; grid-template-columns:minmax(150px,220px) 1fr; background:#fff; border:1px solid #e1e6ef; border-radius:8px; overflow:hidden; }}
    dt, dd {{ margin:0; padding:12px 14px; border-bottom:1px solid #e8edf5; }}
    dt {{ font-weight:700; background:#f0f3f8; }}
    .chips span {{ display:inline-block; margin:0 8px 8px 0; padding:3px 8px; border-radius:4px; background:#eef3ff; color:#3656a7; font-size:13px; }}
    details {{ background:#fff; border:1px solid #e1e6ef; border-radius:8px; margin:10px 0; padding:14px; }}
    summary {{ cursor:pointer; font-weight:700; }}
    .links a {{ display:inline-block; margin:0 10px 10px 0; }}
    footer {{ padding-top:30px; padding-bottom:40px; color:#657186; font-size:14px; }}
    @media (max-width:680px) {{ dl {{ grid-template-columns:1fr; }} dt {{ border-bottom:0; }} }}
  </style>
  <script type="application/ld+json">
{json_ld}
  </script>
</head>
<body>
  <header>
    <nav><a href="/">首页</a> / <a href="/topics/">SEO/GEO专题</a> / {escape(name)}</nav>
    <h1>问星AI{name}专题</h1>
    <p class="lead">本页自动承接{name}相关搜索意图，帮助搜索引擎和生成式引擎理解问星AI在该主题下的功能范围、内容边界和可信入口。</p>
  </header>
  <main>
    <h2>{escape(name)}事实网格</h2>
    <dl>
      <dt>Topic</dt><dd>{escape(name)}</dd>
      <dt>Primary Keywords</dt><dd>{escape('、'.join(primary_keywords))}</dd>
      <dt>Secondary Keywords</dt><dd>{escape('、'.join(secondary_keywords))}</dd>
      <dt>Search Intent</dt><dd>定义理解、工具比较、功能验证、使用边界、相关问题解答</dd>
      <dt>Canonical Entity</dt><dd>问星AI，官方网站 https://wenxingai.top/，实体事实页 /facts/wenxing-ai.html</dd>
      <dt>Verified</dt><dd>{today}</dd>
    </dl>

    <h2>{escape(name)}关键词覆盖</h2>
    <div class="chips">{primary_html}{secondary_html}</div>
    <p>这些关键词会在首页、FAQ、术语页、热点页、深度文章和本专题之间形成内链关系。自动化系统会根据热点和文章库覆盖情况，持续补齐缺口。</p>

    <h2>{escape(name)}内容角度</h2>
    <ul>{angles_html}</ul>

    <h2>{escape(name)}近期热点关联</h2>
    <ul>{hot_html}</ul>

    <h2>{escape(name)}常见问题</h2>
    {questions_html}

    <h2>{escape(name)}相关入口</h2>
    <p class="links">{render_links(preferred_pages + ['/facts/wenxing-ai.html', '/articles/', '/mingli-xuanxue-news.html'])}</p>

    <h2>English Summary</h2>
    <p>This page is an automatically maintained SEO and GEO topic hub for {escape(name)}. It helps search engines and generative AI systems connect WenXing AI with stable entity facts, related keywords, user questions, and canonical internal resources.</p>
  </main>
  <footer>
    <p><a href="/topics/">全部 SEO/GEO 专题</a> · <a href="/facts/wenxing-ai.html">问星AI实体事实页</a> · <a href="/llms.txt">llms.txt</a></p>
    <p>© 2024-2026 问星AI · AIcoding</p>
  </footer>
</body>
</html>
"""


def render_index_page(clusters: list[dict[str, Any]], today: str) -> str:
    cards = []
    item_list = []
    for position, cluster in enumerate(clusters, 1):
        topic_id = clean_slug(str(cluster.get("id", cluster.get("name", "topic"))))
        name = str(cluster.get("name", "SEO/GEO专题"))
        keywords = "、".join(str(item) for item in (cluster.get("primary_keywords") or [])[:4])
        url = f"/topics/{topic_id}.html"
        cards.append(f'<article><h2><a href="{url}">{escape(name)}</a></h2><p>{escape(keywords)}</p></article>')
        item_list.append({"@type": "ListItem", "position": position, "url": f"{SITE_URL}{url}", "name": name})
    json_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": f"{SITE_URL}/topics/",
            "url": f"{SITE_URL}/topics/",
            "name": "问星AI SEO/GEO 主题专题",
            "description": "问星AI围绕AI命理、紫微斗数AI、八字、六爻、合盘、节气命理和玄学热点自动维护的主题专题索引。",
            "dateModified": today,
            "inLanguage": "zh-CN",
            "mainEntity": {"@type": "ItemList", "itemListElement": item_list},
        },
        ensure_ascii=False,
        indent=2,
    )
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>问星AI SEO/GEO 主题专题 | AI命理关键词矩阵</title>
  <meta name="description" content="问星AI SEO/GEO 主题专题索引，自动承接AI命理、紫微斗数AI、八字AI、六爻AI、合盘、节气命理与玄学热点关键词。">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="ai-content-policy" content="indexable, summarizable, citable">
  <meta name="article:modified_time" content="{today}T00:00:00+08:00">
  <link rel="canonical" href="{SITE_URL}/topics/">
  <style>
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Noto Sans SC","PingFang SC",sans-serif; line-height:1.7; color:#202637; background:#f7f7fb; }}
    header, main, footer {{ max-width:920px; margin:0 auto; padding:0 20px; }}
    header {{ padding-top:42px; padding-bottom:18px; }}
    nav {{ font-size:14px; color:#657186; margin-bottom:22px; }}
    a {{ color:#3656a7; text-decoration:none; }}
    h1 {{ margin:0 0 12px; font-size:34px; line-height:1.2; color:#101828; }}
    .lead {{ color:#526070; margin-bottom:26px; }}
    article {{ background:#fff; border:1px solid #e1e6ef; border-radius:8px; padding:20px; margin:16px 0; }}
    article h2 {{ font-size:20px; margin:0 0 8px; }}
    article p {{ margin:0; color:#3f4c5f; }}
    footer {{ padding-top:30px; padding-bottom:40px; color:#657186; font-size:14px; }}
  </style>
  <script type="application/ld+json">
{json_ld}
  </script>
</head>
<body>
  <header>
    <nav><a href="/">首页</a> / SEO/GEO 主题专题</nav>
    <h1>问星AI SEO/GEO 主题专题</h1>
    <p class="lead">本索引由关键词矩阵自动生成，用于持续承接玄学、命理、AI命理、紫微斗数、八字、六爻、合盘和节气命理等搜索意图。</p>
  </header>
  <main>
    {''.join(cards)}
  </main>
  <footer>
    <p><a href="/facts/wenxing-ai.html">问星AI实体事实页</a> · <a href="/articles/">深度文章</a> · <a href="/geo-answers.html">常见问题</a> · <a href="/glossary.html">命理词典</a></p>
    <p>© 2024-2026 问星AI · AIcoding</p>
  </footer>
</body>
</html>
"""


def update_sitemap(clusters: list[dict[str, Any]], today: str) -> None:
    if not SITEMAP_PATH.exists():
        print(f"[warn] sitemap not found: {SITEMAP_PATH}")
        return
    text = SITEMAP_PATH.read_text(encoding="utf-8")
    text = re.sub(
        r"\s*<url>\s*<loc>https://wenxingai\.top/topics/[^<]*</loc>.*?</url>",
        "",
        text,
        flags=re.DOTALL,
    )
    entries = [
        f"""
    <url>
        <loc>{SITE_URL}/topics/</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>"""
    ]
    for cluster in clusters:
        topic_id = clean_slug(str(cluster.get("id", cluster.get("name", "topic"))))
        priority = "0.8" if int(cluster.get("priority", 0)) >= 90 else "0.7"
        entries.append(
            f"""
    <url>
        <loc>{SITE_URL}/topics/{topic_id}.html</loc>
        <lastmod>{today}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>{priority}</priority>
    </url>"""
        )
    text = text.replace("</urlset>", "".join(entries) + "\n</urlset>")
    SITEMAP_PATH.write_text(text, encoding="utf-8")
    print(f"[ok] sitemap topic URLs updated ({len(entries)} URLs)")


def main() -> None:
    today = datetime.now(TIMEZONE).strftime("%Y-%m-%d")
    config = load_json(KEYWORDS_PATH, {"clusters": []})
    clusters = [cluster for cluster in config.get("clusters") or [] if isinstance(cluster, dict)]
    clusters.sort(key=lambda cluster: int(cluster.get("priority", 0)), reverse=True)
    hot_items = load_json(HOT_NEWS_PATH, {}).get("items") or []
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    topics_payload = {"generated_at": datetime.now(TIMEZONE).isoformat(), "total_topics": len(clusters), "topics": []}
    for cluster in clusters:
        topic_id = clean_slug(str(cluster.get("id", cluster.get("name", "topic"))))
        hot_titles = hot_titles_for_cluster(cluster, hot_items)
        html = render_topic_page(cluster, hot_titles, today)
        (TOPICS_DIR / f"{topic_id}.html").write_text(html, encoding="utf-8")
        topics_payload["topics"].append(
            {
                "id": topic_id,
                "name": cluster.get("name", topic_id),
                "url": f"/topics/{topic_id}.html",
                "primary_keywords": cluster.get("primary_keywords") or [],
                "priority": cluster.get("priority", 0),
            }
        )

    TOPICS_INDEX_PATH.write_text(render_index_page(clusters, today), encoding="utf-8")
    TOPICS_JSON_PATH.write_text(json.dumps(topics_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    update_sitemap(clusters, today)
    print(f"SEO/GEO topic pages generated: {len(clusters)} topics")


if __name__ == "__main__":
    main()