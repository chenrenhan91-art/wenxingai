#!/usr/bin/env python3
"""
generate_article_from_snippets.py

将每日社交内容 snippet 扩展为完整的 SEO 优化深解文章。
输入：gemini-content-bundle.json（社交文案 + 热点摘要）
输出：
  - generated/articles/{slug}.md （Markdown 文章）
  - generated/articles/{slug}.html （HTML 页面）
  - generated/articles-index.json （文章索引）
  - 更新 index.html 的"深度文章"导航
"""

from __future__ import annotations

import json
import os
import re
import socket
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "hot-news-data.json"
CONTENT_BUNDLE_PATH = ROOT / "generated" / "gemini-content-bundle.json"
ARTICLES_DIR = ROOT / "generated" / "articles"
ARTICLES_INDEX_PATH = ROOT / "generated" / "articles-index.json"
ARTICLES_REPORT_PATH = ROOT / "generated" / "articles-report.md"

ARTICLES_DIR.mkdir(exist_ok=True)

DEFAULT_MODEL = "deepseek-v4-flash"
DASHSCOPE_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_RETRY_ATTEMPTS = 3

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0 Safari/537.36"
)


def get_gemini_client() -> str | None:
    """获取 DashScope API Key"""
    return os.getenv("DASHSCOPE_API_KEY") or None


def build_article_generation_schema() -> dict[str, Any]:
    """定义文章生成的 JSON schema"""
    return {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "文章标题（40-60 字，包含主关键词）"
            },
            "seo_title": {
                "type": "string",
                "description": "SEO 标题（50-60 字，用于 <title> 标签）"
            },
            "seo_description": {
                "type": "string",
                "description": "Meta 描述（150-160 字）"
            },
            "keywords": {
                "type": "array",
                "items": {"type": "string"},
                "description": "SEO 关键词列表（5-8 个）"
            },
            "excerpt": {
                "type": "string",
                "description": "文章摘要（100-150 字）"
            },
            "body_html": {
                "type": "string",
                "description": "完整文章 HTML 体（包含 <h2>, <p>, <blockquote> 等，2000-3000 字）"
            },
            "faq_items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string"},
                        "answer": {"type": "string"}
                    },
                    "required": ["question", "answer"]
                },
                "description": "常见问题（3-5 个）"
            },
            "internal_links": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "url": {"type": "string"},
                        "context": {"type": "string"}
                    },
                    "required": ["text", "url"]
                },
                "description": "内链建议（3-5 个）"
            },
            "cta_primary": {
                "type": "string",
                "description": "主要 CTA（立即体验问星AI）"
            },
            "cta_secondary": {
                "type": "string",
                "description": "次要 CTA（或相关推荐）"
            }
        },
        "required": [
            "title", "seo_title", "seo_description", "keywords", "excerpt",
            "body_html", "faq_items", "internal_links", "cta_primary", "cta_secondary"
        ]
    }


def load_content_bundle() -> dict[str, Any] | None:
    """加载社交内容包"""
    if not CONTENT_BUNDLE_PATH.exists():
        print(f"[error] {CONTENT_BUNDLE_PATH} not found")
        return None
    
    try:
        with open(CONTENT_BUNDLE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[error] failed to load content bundle: {e}")
        return None


def slugify(text: str) -> str:
    """将文本转换为 URL slug"""
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def build_article_prompt(
    bundle: dict[str, Any],
    locale: str
) -> str:
    """构建文章生成 prompt"""
    
    input_items = bundle.get('input_items', [])[:6]  # 取前 6 条热点
    social_context = bundle.get('localizations', {}).get(locale, {})
    
    # 收集热点摘要
    hot_topics = "\n".join([
        f"- {item.get('title', '')}"
        for item in input_items
    ])
    
    # 社交文案作为参考
    site_article = social_context.get('site_article', {})
    social_excerpt = site_article.get('excerpt', '')
    
    locale_name = "普通话（简体中文）" if locale == "zh_cn" else "繁体中文"
    
    return f"""你是问星AI的资深玄学评论员兼内容编辑。

今日（{datetime.now(ZoneInfo('Asia/Taipei')).strftime('%Y年%m月%d日')}）热点新闻聚焦：

{hot_topics}

你需要基于上述热点，生成一篇深度解读文章，语言为{locale_name}。

要求：
1. 文章长度 2000-3000 字，分为 3-5 个主要段落
2. 每个段落标题使用 <h2> 标签，内容段落使用 <p> 标签
3. 在关键处插入 <strong> 加粗的概念词汇
4. 引用的新闻标题可用 <em> 斜体
5. 包含 3-5 个常见问题（FAQ）
6. 在文末附上指向本站其他页面的内链建议
7. 主 CTA：鼓励用户访问问星AI网站体验"AI 命理趋势分析"
8. 核心观点：不是预言师，而是帮助理解个人周期与流年关系

社交文案参考角度：
"{social_excerpt}"

你的文章应该：
- 深入挖掘这个热点背后的玄学原理
- 对比"传统宿命论"vs"AI 趋势分析"的差异
- 鼓励读者用理性视角重新认识命理
- 避免夸大其词，避免做出绝对预言

输出必须是有效的 JSON，严格符合定义的 schema。"""


def generate_article_with_gemini(
    bundle: dict[str, Any],
    locale: str,
    client: str | None,
    model: str = DEFAULT_MODEL
) -> dict[str, Any] | None:
    """使用 DashScope 生成完整文章"""

    if not client:
        return None

    prompt = build_article_prompt(bundle, locale)

    try:
        request_payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "response_format": {"type": "json_object"},
        }
        req = urllib.request.Request(
            DASHSCOPE_ENDPOINT,
            data=json.dumps(request_payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {client}",
                "User-Agent": USER_AGENT,
            },
            method="POST",
        )
        last_exc: Exception | None = None
        for attempt in range(1, DEFAULT_RETRY_ATTEMPTS + 1):
            try:
                with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT_SECONDS) as resp:
                    response_payload = json.loads(resp.read().decode("utf-8"))
                    break
            except (HTTPError, URLError, socket.timeout, TimeoutError) as exc:
                last_exc = exc
                if attempt >= DEFAULT_RETRY_ATTEMPTS:
                    raise
                time.sleep(min(2 * attempt, 6))

        choices = response_payload.get("choices", [])
        if not choices:
            raise RuntimeError("DashScope returned no choices")
        text = choices[0].get("message", {}).get("content", "").strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        return json.loads(text)

    except Exception as e:
        print(f"[error] failed to generate article for {locale}: {e}")
        return None


def generate_html_page(
    article: dict[str, Any],
    slug: str,
    locale: str,
    published_at: str
) -> str:
    """生成完整的 HTML 页面"""
    
    title = article.get('title', '热点解读')
    seo_title = article.get('seo_title', title)
    seo_desc = article.get('seo_description', '')
    keywords = ', '.join(article.get('keywords', []))
    body_html = article.get('body_html', '')
    excerpt = article.get('excerpt', '')
    faq_items = article.get('faq_items', [])
    internal_links = article.get('internal_links', [])
    cta_primary = article.get('cta_primary', '')
    cta_secondary = article.get('cta_secondary', '')
    
    # 构建 FAQ 的 JSON-LD
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item['question'],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item['answer']
                }
            }
            for item in faq_items
        ]
    }
    
    # 构建 Article 的 JSON-LD
    article_schema = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": seo_title,
        "description": seo_desc,
        "image": "https://wenxingai.top/share-cover.jpg",
        "datePublished": published_at,
        "author": {
            "@type": "Organization",
            "name": "问星AI"
        }
    }
    
    # 构建 FAQ HTML
    faq_html_items = []
    for item in faq_items:
        faq_html_items.append(f'<div class="faq-item"><strong>Q: {item["question"]}</strong><p>{item["answer"]}</p></div>')
    faq_html = ''.join(faq_html_items)
    
    # 构建内链 HTML
    internal_links_html = ''
    if internal_links:
        link_items = []
        for link in internal_links:
            link_text = link.get("text", "")
            link_url = link.get("url", "#")
            link_items.append(f'<a href="{link_url}">{link_text}</a>')
        internal_links_html = f'<div class="internal-links"><h4>相关阅读</h4>{"".join(link_items)}</div>'
    
    # 确定语言
    lang = 'zh-CN' if locale == 'zh_cn' else 'zh-TW'
    
    # 构建文章 schema JSON
    article_schema_json = json.dumps(article_schema, ensure_ascii=False, indent=2)
    faq_schema_json = json.dumps(faq_schema, ensure_ascii=False, indent=2)
    
    # 组合 HTML
    html = (
        f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{seo_title}</title>
    <meta name="description" content="{seo_desc}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="https://wenxingai.top/articles/{slug}.html">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{excerpt}">
    <meta property="og:image" content="https://wenxingai.top/share-cover.jpg">
    <meta property="og:url" content="https://wenxingai.top/articles/{slug}.html">
    
    <!-- JSON-LD 结构化数据 -->
    <script type="application/ld+json">
{article_schema_json}
    </script>
    <script type="application/ld+json">
{faq_schema_json}
    </script>
    
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.8;
            color: #333;
            background: #f5f5f5;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 20px; background: white; }}
        .article-header {{ margin-bottom: 40px; border-bottom: 2px solid #e0e0e0; padding-bottom: 20px; }}
        .article-header h1 {{ font-size: 2em; margin-bottom: 10px; color: #1a1a1a; }}
        .article-meta {{ color: #666; font-size: 0.9em; }}
        .article-content {{ margin: 40px 0; }}
        .article-content h2 {{ 
            font-size: 1.5em; 
            margin: 30px 0 15px 0; 
            color: #1a1a1a;
            border-left: 4px solid #720e53;
            padding-left: 15px;
        }}
        .article-content p {{ 
            margin-bottom: 15px; 
            text-align: justify;
        }}
        .article-content strong {{ color: #720e53; font-weight: 600; }}
        .article-content em {{ font-style: italic; color: #666; }}
        
        .faq-section {{ margin: 40px 0; background: #f9f9f9; padding: 20px; border-radius: 8px; }}
        .faq-section h3 {{ margin-bottom: 20px; color: #1a1a1a; }}
        .faq-item {{ margin-bottom: 20px; }}
        .faq-item strong {{ display: block; margin-bottom: 8px; color: #720e53; }}
        .faq-item p {{ color: #666; margin-left: 15px; }}
        
        .internal-links {{ 
            background: #f0f0f0; 
            padding: 20px; 
            border-radius: 8px;
            margin: 40px 0;
        }}
        .internal-links h4 {{ margin-bottom: 15px; color: #1a1a1a; }}
        .internal-links a {{ 
            display: block; 
            margin: 8px 0;
            color: #0066cc;
            text-decoration: none;
        }}
        .internal-links a:hover {{ text-decoration: underline; }}
        
        .cta-box {{
            background: linear-gradient(135deg, #720e53, #a01566);
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin: 40px 0;
            text-align: center;
        }}
        .cta-box p {{ margin-bottom: 15px; }}
        .cta-button {{
            display: inline-block;
            background: white;
            color: #720e53;
            padding: 12px 30px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }}
        .cta-button:hover {{ transform: scale(1.05); }}
        .cta-secondary {{ 
            display: inline-block;
            color: #ddd;
            margin-top: 15px;
            font-size: 0.9em;
        }}
        
        .breadcrumb {{ color: #999; font-size: 0.9em; margin-bottom: 20px; }}
        .breadcrumb a {{ color: #0066cc; text-decoration: none; }}
        
        footer {{ 
            margin-top: 60px; 
            padding-top: 20px; 
            border-top: 1px solid #e0e0e0;
            color: #999;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="breadcrumb">
            <a href="/">首页</a> / <a href="/mingli-xuanxue-news.html">热点新闻</a> / {title}
        </div>
        
        <article>
            <div class="article-header">
                <h1>{title}</h1>
                <div class="article-meta">
                    发布于 {published_at} | 分类：热点解读
                </div>
            </div>
            
            <div class="article-content">
{body_html}
            </div>
            
            <div class="faq-section">
                <h3>常见问题</h3>
                {faq_html}
            </div>
            
            <div class="cta-box">
                <p>{cta_primary}</p>
                <a href="https://wenxingai.top/?utm_source=article&utm_medium=cta&utm_campaign=article-{slug}" class="cta-button">
                    立即体验问星AI
                </a>
                <div class="cta-secondary">{cta_secondary}</div>
            </div>
            
            {internal_links_html}
        </article>
        
        <footer>
            <p>本文由问星AI自动生成。观点基于当日热点新闻分析，仅供参考。</p>
            <p><a href="/mingli-xuanxue-news.html">返回热点新闻</a></p>
        </footer>
    </div>
</body>
</html>"""
    )
    
    return html


def generate_markdown_article(
    article: dict[str, Any],
    slug: str
) -> str:
    """生成 Markdown 格式的文章"""
    
    title = article.get('title', '热点解读')
    excerpt = article.get('excerpt', '')
    body_html = article.get('body_html', '')
    faq_items = article.get('faq_items', [])
    keywords = ', '.join(article.get('keywords', []))
    cta_primary = article.get('cta_primary', '')
    
    # 简单转换 HTML 为 Markdown（这里是简化版）
    body_md = body_html.replace('<h2>', '## ').replace('</h2>', '')
    body_md = body_md.replace('<p>', '').replace('</p>', '\n\n')
    body_md = body_md.replace('<strong>', '**').replace('</strong>', '**')
    body_md = body_md.replace('<em>', '_').replace('</em>', '_')
    
    faq_md = '\n'.join([
        f"**Q: {item['question']}**\n\n{item['answer']}\n"
        for item in faq_items
    ])
    
    markdown = f"""# {title}

> {excerpt}

**关键词**: {keywords}

---

{body_md}

## 常见问题

{faq_md}

---

**CTA**: {cta_primary}

**链接**: https://wenxingai.top/articles/{slug}.html
"""
    
    return markdown


def save_article_metadata(
    articles_metadata: list[dict[str, Any]],
    stats: dict[str, Any]
) -> None:
    """保存文章索引和报告"""
    
    # 保存索引
    index_data = {
        "generated_at": datetime.now(ZoneInfo('Asia/Taipei')).isoformat(),
        "total_articles": len(articles_metadata),
        "articles": articles_metadata,
    }
    
    with open(ARTICLES_INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    print(f"[ok] saved articles index to {ARTICLES_INDEX_PATH}")
    
    # 生成报告
    report = f"""# 文章生成报告 {datetime.now(ZoneInfo('Asia/Taipei')).strftime('%Y-%m-%d %H:%M')}

## 摘要
- 总文章数: {stats['total_generated']}
- 成功: {stats['success']}
- 失败: {stats['failed']}
- Gemini 执行: {'是' if stats.get('gemini_executed') else '否'}

## 生成的文章

"""
    
    for meta in articles_metadata:
        report += f"""### {meta['title']}
- 语言: {meta['locale']}
- 路径: {meta['html_path']}
- 关键词: {', '.join(meta.get('keywords', []))}

"""
    
    with open(ARTICLES_REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"[ok] saved articles report to {ARTICLES_REPORT_PATH}")


def main() -> None:
    """主函数"""
    
    print("[info] starting article generation from snippets...")
    
    # 加载内容包
    bundle = load_content_bundle()
    if not bundle:
        print("[skip] no content bundle found, exiting")
        return
    
    bundle_slug = bundle.get('slug', 'daily-content')
    published_at = bundle.get('generated_at_display', datetime.now(ZoneInfo('Asia/Taipei')).strftime('%Y年%m月%d日'))
    
    # 初始化 DashScope
    client = get_gemini_client()
    if not client:
        print("[warn] DASHSCOPE_API_KEY not available, skipping article generation")
        return
    
    print(f"[info] generating articles for campaign: {bundle_slug}")
    
    articles_metadata = []
    stats = {
        'total_generated': 0,
        'success': 0,
        'failed': 0,
        'gemini_executed': True,
    }
    
    # 为每个语言版本生成文章
    for locale in ['zh_cn', 'zh_hant']:
        print(f"\n[info] generating article for locale: {locale}")
        
        # 生成文章内容
        article_data = generate_article_with_gemini(bundle, locale, client)
        if not article_data:
            stats['failed'] += 1
            continue
        
        # 生成 slug
        article_slug = f"{bundle_slug}-{locale}"
        
        # 生成 HTML
        html_content = generate_html_page(article_data, article_slug, locale, published_at)
        html_path = ARTICLES_DIR / f"{article_slug}.html"
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[ok] generated HTML article: {html_path}")
        
        # 生成 Markdown
        md_content = generate_markdown_article(article_data, article_slug)
        md_path = ARTICLES_DIR / f"{article_slug}.md"
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"[ok] generated Markdown article: {md_path}")
        
        # 记录元数据
        meta = {
            'slug': article_slug,
            'title': article_data.get('title', ''),
            'locale': locale,
            'html_path': f"/articles/{article_slug}.html",
            'md_path': f"/articles/{article_slug}.md",
            'keywords': article_data.get('keywords', []),
            'seo_title': article_data.get('seo_title', ''),
            'published_at': published_at,
        }
        articles_metadata.append(meta)
        
        stats['success'] += 1
        stats['total_generated'] += 1
    
    # 保存索引和报告
    save_article_metadata(articles_metadata, stats)
    
    print(f"\n[ok] article generation completed")
    print(f"    total: {stats['total_generated']} | success: {stats['success']} | failed: {stats['failed']}")


if __name__ == '__main__':
    main()
