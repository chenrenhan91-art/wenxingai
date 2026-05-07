#!/usr/bin/env python3
"""
generate_blog_articles.py

基于当日热点新闻，为知乎、百家号、简书三个博客平台生成外链文章草稿。
生成的文章供手动发布，每篇自然内嵌 1-2 处问星AI外链。

输出目录：generated/blog-articles/YYYY-MM-DD/
  - zhihu.md        知乎文章草稿
  - baijiahao.md    百家号文章草稿
  - jianshu.md      简书文章草稿
  - meta.json       本次生成的元数据（主题、关键词等）
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
PROMPT_PATH = ROOT / "prompts" / "blog_outreach_prompt.txt"
BLOG_ARTICLES_DIR = ROOT / "generated" / "blog-articles"

DEFAULT_MODEL = "gemini-2.5-pro"
DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_RETRY_ATTEMPTS = 3
SITE_URL = "https://wenxingai.top"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0 Safari/537.36"
)

BLOG_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "topic": {"type": "string"},
        "hot_keywords": {"type": "array", "items": {"type": "string"}},
        "articles": {
            "type": "object",
            "properties": {
                "zhihu": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "platform_note": {"type": "string"},
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "cta": {"type": "string"},
                    },
                    "required": ["title", "platform_note", "body_markdown", "tags", "cta"],
                },
                "baijiahao": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "platform_note": {"type": "string"},
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "cta": {"type": "string"},
                    },
                    "required": ["title", "platform_note", "body_markdown", "tags", "cta"],
                },
                "jianshu": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "platform_note": {"type": "string"},
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "cta": {"type": "string"},
                    },
                    "required": ["title", "platform_note", "body_markdown", "tags", "cta"],
                },
            },
            "required": ["zhihu", "baijiahao", "jianshu"],
        },
    },
    "required": ["topic", "hot_keywords", "articles"],
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


def call_gemini(prompt: str, api_key: str, model: str) -> dict[str, Any]:
    endpoint = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{urllib.parse.quote(model, safe='')}:generateContent"
    )
    request_payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": BLOG_SCHEMA,
        },
    }
    req = urllib.request.Request(
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
            with urllib.request.urlopen(req, timeout=timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, socket.timeout, TimeoutError) as exc:
            last_exc = exc
            if attempt >= DEFAULT_RETRY_ATTEMPTS:
                break
            time.sleep(min(2 * attempt, 6))
    assert last_exc is not None
    raise last_exc


def extract_json(response_payload: dict[str, Any]) -> dict[str, Any]:
    texts: list[str] = []
    for candidate in response_payload.get("candidates", []):
        content = candidate.get("content") or {}
        for part in content.get("parts", []):
            text = part.get("text", "").strip()
            if text:
                texts.append(text)
    raw = "\n".join(texts)
    return json.loads(strip_code_fences(raw))


def load_news() -> dict[str, Any]:
    if not DATA_PATH.exists():
        return {}
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def build_prompt(news_payload: dict[str, Any], today: str) -> str:
    template = PROMPT_PATH.read_text(encoding="utf-8")
    items = news_payload.get("items", [])[:12]
    return template.format(
        today=today,
        news_json=json.dumps(items, ensure_ascii=False, indent=2),
    )


def write_platform_md(out_dir: Path, platform: str, article: dict[str, Any], today: str) -> None:
    title = article.get("title", "")
    tags = article.get("tags", [])
    note = article.get("platform_note", "")
    body = article.get("body_markdown", "")
    cta = article.get("cta", "")

    lines = [
        f"# {title}",
        "",
        f"> 平台：{platform}  |  生成日期：{today}",
        f"> 发布说明：{note}",
        "",
    ]
    if tags:
        lines += [f"**标签**：{'、'.join(tags)}", ""]

    lines += [body.strip(), ""]

    if cta:
        lines += ["---", "", f"> **{cta}**", ""]

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{platform}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] {platform}.md saved to {out_dir}")


def main() -> None:
    load_env_files()

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        print("[error] GEMINI_API_KEY not set — skipping blog article generation")
        return

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    tz = ZoneInfo("Asia/Shanghai")
    today = datetime.now(tz).strftime("%Y-%m-%d")

    out_dir = BLOG_ARTICLES_DIR / today
    meta_path = out_dir / "meta.json"

    # 已生成过当天的草稿则跳过（除非强制刷新）
    force = os.getenv("PIPELINE_FORCE_REFRESH", "").strip().lower() in {"1", "true", "yes"}
    if not force and meta_path.exists():
        print(f"[skip] blog articles for {today} already generated")
        return

    news = load_news()
    if not news.get("items"):
        print("[warn] hot-news-data.json has no items — skipping")
        return

    prompt = build_prompt(news, today)
    print(f"[info] calling Gemini ({model}) for blog articles …")

    response = call_gemini(prompt, api_key, model)
    payload = extract_json(response)

    topic = payload.get("topic", "")
    keywords = payload.get("hot_keywords", [])
    articles = payload.get("articles", {})

    platform_labels = {
        "zhihu": "知乎",
        "baijiahao": "百家号",
        "jianshu": "简书",
    }
    for key, label in platform_labels.items():
        art = articles.get(key)
        if art:
            write_platform_md(out_dir, key, art, today)

    meta = {
        "generated_at": datetime.now(tz).isoformat(),
        "date": today,
        "topic": topic,
        "hot_keywords": keywords,
        "model": model,
        "site_url": SITE_URL,
        "platforms": list(platform_labels.keys()),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] meta.json saved — topic: {topic}")
    print(f"[done] blog articles generated in {out_dir}")


if __name__ == "__main__":
    main()
