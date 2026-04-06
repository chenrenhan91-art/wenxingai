#!/usr/bin/env python3

from __future__ import annotations

import base64
import html
import json
import os
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from collections import Counter
from typing import Iterable
from urllib.parse import urljoin
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "hot-news-sources.json"
DATA_PATH = ROOT / "hot-news-data.json"
INDEX_PATH = ROOT / "index.html"
PAGE_PATH = ROOT / "mingli-xuanxue-news.html"
SITEMAP_PATH = ROOT / "sitemap.xml"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0 Safari/537.36"
)


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
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


CATEGORY_KEYWORDS = {
    "命理新闻": [
        "命理",
        "命理師",
        "命理师",
        "算命",
        "流年",
        "運勢",
        "运势",
        "開運",
        "开运",
        "補庫",
        "补库",
    ],
    "八字紫微": [
        "八字",
        "紫微",
        "斗數",
        "斗数",
        "命盤",
        "命盘",
        "大運",
        "大运",
        "流年",
        "十神",
        "合盤",
        "合盘",
    ],
    "风水玄学": [
        "玄學",
        "玄学",
        "風水",
        "风水",
        "磁場",
        "磁场",
        "民俗",
        "能量",
        "招財",
        "招财",
        "改運",
        "改运",
    ],
    "塔罗星象": [
        "塔羅",
        "塔罗",
        "占卜",
        "星座",
        "桃花",
        "戀愛",
        "恋爱",
        "本週運勢",
        "本周运势",
    ],
    "社区热议": [
        "熱議",
        "热议",
        "討論",
        "讨论",
        "問卦",
        "问卦",
        "閒聊",
        "闲聊",
        "求助",
        "原理",
        "準嗎",
        "准吗",
    ],
}

EXCLUDED_KEYWORDS = [
    "柯文哲",
    "總統",
    "总统",
    "大選",
    "大选",
    "立委",
    "立法委員",
    "立法委员",
    "政黨",
    "政党",
    "選舉",
    "选举",
    "政治",
    "國民黨",
    "民進黨",
    "民进党",
    "民眾黨",
    "民众党",
    "道教",
    "佛教",
    "宗教",
    "宮廟",
    "宫庙",
    "法會",
    "法会",
    "開光",
    "开光",
    "誦經",
    "诵经",
    "住持",
    "主教",
    "神像",
    "神明",
    "香火",
    "禮佛",
    "礼佛",
    "土地公",
    "佛光山",
    "廟會",
    "庙会",
]

SOURCE_WEIGHTS = {
    "google_news_mingli_tw": 6.2,
    "google_news_xuanxue_tw": 6.0,
    "google_news_taluo_tw": 5.8,
    "google_news_fengshui_tw": 5.8,
    "ptt_gossiping": 5.4,
    "ptt_womentalk": 5.1,
    "ptt_marvel": 4.6,
    "youtube_search": 5.4,
    "x_recent_search": 5.2,
    "reddit_search": 4.8,
}

FALLBACK_ITEMS = [
    {
        "title": "台湾媒体与海外华语社区的命理热议，会优先整理在这里",
        "summary": "当可核验来源当天的高相关内容较少时，页面会保留最近一轮值得追踪的话题，保证阅读节奏与版面完整。",
        "url": "https://wenxingai.top/mingli-xuanxue-news.html",
        "source_id": "fallback_watch",
        "source": "问星AI观察",
        "source_url": "https://wenxingai.top/mingli-xuanxue-news.html",
        "source_group": "editorial",
        "category": "趋势观察",
        "published": None,
        "published_display": "持续更新",
        "matched_keywords": ["命理", "玄学", "台湾热点"],
        "score": 0.0,
    }
]


@dataclass
class NewsItem:
    title: str
    summary: str
    url: str
    source_id: str
    source: str
    source_url: str
    source_group: str
    category: str
    published: str | None
    published_display: str
    matched_keywords: list[str]
    score: float


def fetch_text(url: str, headers: dict[str, str] | None = None) -> str:
    last_error: Exception | None = None
    for _ in range(3):
        try:
            req_headers = {"User-Agent": USER_AGENT, "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8"}
            if headers:
                req_headers.update(headers)
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=20) as response:
                return response.read().decode("utf-8", "ignore")
        except Exception as exc:
            last_error = exc
    if last_error:
        raise last_error
    raise RuntimeError(f"failed to fetch text from {url}")


def fetch_bytes(url: str, headers: dict[str, str] | None = None) -> bytes:
    last_error: Exception | None = None
    for _ in range(3):
        try:
            req_headers = {"User-Agent": USER_AGENT, "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8"}
            if headers:
                req_headers.update(headers)
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=20) as response:
                return response.read()
        except Exception as exc:
            last_error = exc
    if last_error:
        raise last_error
    raise RuntimeError(f"failed to fetch bytes from {url}")


def fetch_json(url: str, headers: dict[str, str] | None = None) -> dict:
    return json.loads(fetch_text(url, headers=headers))


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_title(value: str) -> str:
    return re.sub(r"[\W_]+", "", value)


def build_semantic_fingerprint(title: str, summary: str) -> set[str]:
    text = f"{title} {summary}".lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", " ", text)
    tokens = [token for token in text.split() if len(token) >= 2]
    return set(tokens)


def token_jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def truncate_text(value: str, limit: int = 92) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def parse_date(value: str, timezone: ZoneInfo) -> datetime | None:
    value = (value or "").strip()
    if not value:
        return None

    if value.isdigit():
        try:
            return datetime.fromtimestamp(int(value), tz=timezone)
        except ValueError:
            pass

    try:
        dt = parsedate_to_datetime(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone)
        return dt.astimezone(timezone)
    except Exception:
        pass

    for pattern in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%Y/%m/%d %H:%M:%S",
    ):
        try:
            parsed = datetime.strptime(value, pattern)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone)
            return parsed.astimezone(timezone)
        except ValueError:
            continue
    return None


def format_date(dt: datetime | None, timezone: ZoneInfo) -> tuple[str | None, str]:
    if dt is None:
        return None, "最近更新"
    local = dt.astimezone(timezone)
    return local.strftime("%Y-%m-%d"), local.strftime("%Y-%m-%d")


def score_text(
    title: str,
    summary: str,
    source_id: str,
    category_hint: str | None = None,
) -> tuple[str, list[str], float, bool]:
    haystack = f"{title} {summary}"
    category_scores: dict[str, float] = {}
    matched_keywords: list[str] = []

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0.0
        for keyword in keywords:
            if keyword in title:
                score += 2.2
                matched_keywords.append(keyword)
            elif keyword in haystack:
                score += 1.0
                matched_keywords.append(keyword)
        category_scores[category] = score

    if category_hint:
        category_scores[category_hint] = category_scores.get(category_hint, 0.0) + 1.2

    category = max(category_scores, key=category_scores.get) if category_scores else "趋势观察"
    total_score = category_scores.get(category, 0.0) + SOURCE_WEIGHTS.get(source_id, 0.0)

    unique_keywords: list[str] = []
    for keyword in matched_keywords:
        if keyword not in unique_keywords:
            unique_keywords.append(keyword)

    had_explicit_match = bool(unique_keywords)
    if not unique_keywords:
        unique_keywords = [category_hint or category]

    return category, unique_keywords[:3], total_score, had_explicit_match


def split_google_news_title(value: str) -> tuple[str, str | None]:
    clean = strip_tags(value)
    if " - " not in clean:
        return clean, None
    headline, publisher = clean.rsplit(" - ", 1)
    return headline.strip(), publisher.strip()


def build_google_summary(title: str, description: str, source_name: str) -> str:
    clean_description = strip_tags(description)
    if not clean_description:
        return f"来自 {source_name} 的台湾繁体媒体报道，点击可查看原文。"

    normalized_description = normalize_title(clean_description)
    normalized_title = normalize_title(title)
    if normalized_description.startswith(normalized_title):
        return f"来自 {source_name} 的台湾繁体媒体报道，点击可查看原文。"
    return clean_description


def build_public_platform_summary(platform_name: str) -> str:
    return f"来自 {platform_name} 的公开收录内容，点击可查看原文。"


def build_google_site_search_url(site: str, query: str, days: int) -> str:
    effective_days = max(1, min(days, 30))
    search_query = f"site:{site} {query} when:{effective_days}d"
    return (
        "https://news.google.com/rss/search?q="
        f"{urllib.parse.quote(search_query)}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    )


def parse_google_site_search(
    source: dict,
    timezone: ZoneInfo,
    *,
    site: str,
    platform_name: str,
    queries: list[str],
    require_explicit_match: bool = True,
) -> Iterable[NewsItem]:
    days = source.get("max_age_days", 14)
    source_name = f"{platform_name} · Google News"

    for query in queries:
        feed_url = build_google_site_search_url(site, query, days)
        root = ET.fromstring(fetch_bytes(feed_url))
        items = root.findall("./channel/item")

        for item in items:
            raw_title = item.findtext("title") or ""
            title, _publisher = split_google_news_title(raw_title)
            if not title:
                continue
            if "Results on X | Live Posts & Updates" in title:
                continue

            description = item.findtext("description") or ""
            summary = build_google_summary(title, description, source_name)
            if not strip_tags(summary):
                summary = build_public_platform_summary(platform_name)
            if contains_excluded_terms(title, summary):
                continue

            published = parse_date(item.findtext("pubDate") or "", timezone)
            date_iso, date_display = format_date(published, timezone)
            category, matched_keywords, score, had_explicit_match = score_text(
                title,
                description,
                source["id"],
                source.get("category_hint"),
            )
            query_match = query in f"{title} {summary}"
            if require_explicit_match and not (had_explicit_match or query_match):
                continue
            if query_match and query not in matched_keywords:
                matched_keywords = [query, *matched_keywords][:3]

            yield NewsItem(
                title=title,
                summary=truncate_text(summary, 112),
                url=(item.findtext("link") or "").strip(),
                source_id=source["id"],
                source=source_name,
                source_url=feed_url,
                source_group=source.get("source_group", "news"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + 0.2,
            )


def contains_excluded_terms(title: str, summary: str) -> bool:
    haystack = f"{title} {summary}"
    return any(keyword in haystack for keyword in EXCLUDED_KEYWORDS)


def parse_google_news_rss(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    root = ET.fromstring(fetch_bytes(source["url"]))
    items = root.findall("./channel/item")

    for item in items:
        raw_title = item.findtext("title") or ""
        title, publisher = split_google_news_title(raw_title)
        if not title:
            continue

        description = item.findtext("description") or ""
        published = parse_date(item.findtext("pubDate") or "", timezone)
        date_iso, date_display = format_date(published, timezone)
        category, matched_keywords, score, _ = score_text(
            title,
            description,
            source["id"],
            source.get("category_hint"),
        )

        if publisher:
            source_name = f"{publisher} · Google News"
        else:
            source_name = source["name"]

        summary = build_google_summary(title, description, source_name)
        if contains_excluded_terms(title, summary):
            continue
        yield NewsItem(
            title=title,
            summary=truncate_text(summary, 112),
            url=(item.findtext("link") or "").strip(),
            source_id=source["id"],
            source=source_name,
            source_url=source["url"],
            source_group=source.get("source_group", "news"),
            category=category,
            published=date_iso,
            published_display=date_display,
            matched_keywords=matched_keywords,
            score=score + 0.4,
        )


def parse_ptt_heat(raw_value: str) -> float:
    value = strip_tags(raw_value)
    if not value:
        return 0.0
    if value == "爆":
        return 12.0
    if value.startswith("X"):
        return -3.0
    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_ptt_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    board = source["board"]

    for query in source.get("queries", []):
        search_url = (
            f"https://www.ptt.cc/bbs/{board}/search?page=1&q="
            f"{urllib.parse.quote(query)}"
        )
        content = fetch_text(search_url)
        entries = content.split('<div class="r-ent">')[1:]

        for entry in entries:
            title_match = re.search(r'<div class="title">\s*<a href="([^"]+)">([^<]+)</a>', entry)
            if not title_match or not title_match.group(1):
                continue

            href = title_match.group(1).strip()
            title = strip_tags(title_match.group(2))
            if not title:
                continue

            heat = parse_ptt_heat(re.search(r'<div class="nrec">(.*?)</div>', entry, re.S).group(1) if re.search(r'<div class="nrec">(.*?)</div>', entry, re.S) else "")
            author = strip_tags(re.search(r'<div class="author">(.*?)</div>', entry, re.S).group(1) if re.search(r'<div class="author">(.*?)</div>', entry, re.S) else "")
            timestamp_match = re.search(r"M\.(\d+)\.", href)
            published_dt = (
                datetime.fromtimestamp(int(timestamp_match.group(1)), tz=timezone)
                if timestamp_match
                else None
            )
            date_iso, date_display = format_date(published_dt, timezone)

            summary = (
                f"来自 PTT {board} 的热议帖，围绕「{query}」展开讨论"
                f"{'，推文热度 ' + str(int(heat)) if heat > 0 else ''}"
                f"{'，作者 ' + author if author else ''}。"
            )
            if contains_excluded_terms(title, summary):
                continue
            category, matched_keywords, score, _ = score_text(
                title,
                f"{summary} {query}",
                source["id"],
                source.get("category_hint"),
            )
            if query not in matched_keywords:
                matched_keywords = [query, *matched_keywords][:3]

            yield NewsItem(
                title=title,
                summary=truncate_text(summary, 112),
                url=urljoin("https://www.ptt.cc", href),
                source_id=source["id"],
                source=f"PTT {board}",
                source_url=search_url,
                source_group=source.get("source_group", "community"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + max(heat, 0.0) / 3.0,
            )


def get_reddit_access_token() -> tuple[str, str]:
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", USER_AGENT)
    if not client_id or not client_secret:
        raise RuntimeError("missing Reddit API credentials")

    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
    data = urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("utf-8")
    request = urllib.request.Request(
        "https://www.reddit.com/api/v1/access_token",
        data=data,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": user_agent,
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))
    token = payload.get("access_token")
    if not token:
        raise RuntimeError("failed to obtain Reddit access token")
    return token, user_agent


def parse_reddit_public_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WenxingBot/1.0; +https://wenxingai.top)",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
    }

    for query in source.get("queries", []):
        params = urllib.parse.urlencode(
            {"q": query, "sort": "top", "limit": 15, "t": "month", "type": "link"}
        )
        payload = fetch_json(f"https://old.reddit.com/search.json?{params}", headers=headers)

        for child in payload.get("data", {}).get("children", []):
            data = child.get("data", {})
            title = strip_tags(data.get("title") or "")
            if not title:
                continue

            published_dt = datetime.fromtimestamp(data.get("created_utc", 0), tz=timezone)
            date_iso, date_display = format_date(published_dt, timezone)
            ups = int(data.get("ups", 0) or 0)
            comments = int(data.get("num_comments", 0) or 0)
            summary = strip_tags(data.get("selftext") or "")
            summary = summary or (
                f"Reddit 海外社区高热帖子，来自 r/{data.get('subreddit', '')}，"
                f"当前赞成票 {ups}、评论 {comments}。"
            )
            if contains_excluded_terms(title, summary):
                continue
            category, matched_keywords, score, _ = score_text(
                title,
                f"{summary} {query}",
                source["id"],
                source.get("category_hint"),
            )
            metrics_score = ups * 0.05 + comments * 0.08

            yield NewsItem(
                title=title,
                summary=truncate_text(summary, 112),
                url=urljoin("https://old.reddit.com", data.get("permalink", "")),
                source_id=source["id"],
                source=f"Reddit r/{data.get('subreddit', '')}",
                source_url=source["url"],
                source_group=source.get("source_group", "community"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + metrics_score,
            )


def parse_reddit_authenticated_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    token, user_agent = get_reddit_access_token()

    for query in source.get("queries", []):
        params = urllib.parse.urlencode(
            {"q": query, "sort": "top", "limit": 15, "t": "month", "type": "link"}
        )
        payload = fetch_json(
            f"https://oauth.reddit.com/search?{params}",
            headers={
                "Authorization": f"bearer {token}",
                "User-Agent": user_agent,
            },
        )

        for child in payload.get("data", {}).get("children", []):
            data = child.get("data", {})
            title = strip_tags(data.get("title") or "")
            if not title:
                continue

            published_dt = datetime.fromtimestamp(data.get("created_utc", 0), tz=timezone)
            date_iso, date_display = format_date(published_dt, timezone)
            ups = int(data.get("ups", 0) or 0)
            comments = int(data.get("num_comments", 0) or 0)
            summary = strip_tags(data.get("selftext") or "")
            summary = summary or (
                f"Reddit 海外社区高热帖子，来自 r/{data.get('subreddit', '')}，"
                f"当前赞成票 {ups}、评论 {comments}。"
            )
            if contains_excluded_terms(title, summary):
                continue
            category, matched_keywords, score, _ = score_text(
                title,
                f"{summary} {query}",
                source["id"],
                source.get("category_hint"),
            )
            metrics_score = ups * 0.05 + comments * 0.08

            yield NewsItem(
                title=title,
                summary=truncate_text(summary, 112),
                url=urljoin("https://www.reddit.com", data.get("permalink", "")),
                source_id=source["id"],
                source=f"Reddit r/{data.get('subreddit', '')}",
                source_url=source["url"],
                source_group=source.get("source_group", "community"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + metrics_score,
            )


def parse_reddit_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    try:
        yield from parse_reddit_public_search(source, timezone)
        return
    except Exception:
        if not (os.getenv("REDDIT_CLIENT_ID") and os.getenv("REDDIT_CLIENT_SECRET")):
            raise
    yield from parse_reddit_authenticated_search(source, timezone)


def parse_youtube_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        public_queries = source.get("public_queries") or source.get("queries", [])
        yield from parse_google_site_search(
            source,
            timezone,
            site="youtube.com",
            platform_name="YouTube",
            queries=public_queries,
        )
        return

    for query in source.get("queries", []):
        search_params = urllib.parse.urlencode(
            {
                "part": "snippet",
                "q": query,
                "type": "video",
                "maxResults": 12,
                "order": "viewCount",
                "relevanceLanguage": "zh-Hant",
                "regionCode": "TW",
                "key": api_key,
            }
        )
        payload = fetch_json(f"https://www.googleapis.com/youtube/v3/search?{search_params}")
        items = payload.get("items", [])
        video_ids = [item.get("id", {}).get("videoId") for item in items if item.get("id", {}).get("videoId")]
        if not video_ids:
            continue

        stats_params = urllib.parse.urlencode(
            {
                "part": "statistics",
                "id": ",".join(video_ids),
                "key": api_key,
            }
        )
        stats_payload = fetch_json(f"https://www.googleapis.com/youtube/v3/videos?{stats_params}")
        statistics_map = {
            item.get("id"): item.get("statistics", {})
            for item in stats_payload.get("items", [])
            if item.get("id")
        }

        for item in items:
            video_id = item.get("id", {}).get("videoId")
            snippet = item.get("snippet", {})
            title = strip_tags(snippet.get("title") or "")
            if not title or not video_id:
                continue

            published_dt = parse_date(snippet.get("publishedAt") or "", timezone)
            date_iso, date_display = format_date(published_dt, timezone)
            channel_title = strip_tags(snippet.get("channelTitle") or "YouTube")
            statistics = statistics_map.get(video_id, {})
            views = int(statistics.get("viewCount", 0) or 0)
            likes = int(statistics.get("likeCount", 0) or 0)
            comments = int(statistics.get("commentCount", 0) or 0)
            summary = strip_tags(snippet.get("description") or "")
            if not summary:
                summary = (
                    f"YouTube 华语高热视频，来自频道 {channel_title}，"
                    f"当前播放 {views}、点赞 {likes}、评论 {comments}。"
                )
            if contains_excluded_terms(title, summary):
                continue

            category, matched_keywords, score, _ = score_text(
                title,
                f"{summary} {query}",
                source["id"],
                source.get("category_hint"),
            )
            if query not in matched_keywords:
                matched_keywords = [query, *matched_keywords][:3]
            metrics_score = views * 0.00002 + likes * 0.004 + comments * 0.006

            yield NewsItem(
                title=title,
                summary=truncate_text(summary, 112),
                url=f"https://www.youtube.com/watch?v={video_id}",
                source_id=source["id"],
                source=f"YouTube · {channel_title}",
                source_url=source["url"],
                source_group=source.get("source_group", "video"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + metrics_score,
            )


def parse_x_recent_search(source: dict, timezone: ZoneInfo) -> Iterable[NewsItem]:
    token = os.getenv("X_BEARER_TOKEN")
    if not token:
        public_queries = source.get("fallback_queries") or ["命理師", "算命", "紫微", "塔羅"]
        yield from parse_google_site_search(
            source,
            timezone,
            site="x.com",
            platform_name="X",
            queries=public_queries,
        )
        return

    for query in source.get("queries", []):
        params = urllib.parse.urlencode(
            {
                "query": query,
                "max_results": 50,
                "tweet.fields": "created_at,public_metrics,lang",
                "expansions": "author_id",
                "user.fields": "username,name",
            }
        )
        payload = fetch_json(
            f"https://api.x.com/2/tweets/search/recent?{params}",
            headers={"Authorization": f"Bearer {token}"},
        )
        users = {
            user.get("id"): user
            for user in payload.get("includes", {}).get("users", [])
            if user.get("id")
        }

        for tweet in payload.get("data", []):
            text = strip_tags(tweet.get("text") or "").replace("\n", " ").strip()
            if not text:
                continue

            published_dt = parse_date(tweet.get("created_at") or "", timezone)
            date_iso, date_display = format_date(published_dt, timezone)
            user = users.get(tweet.get("author_id"), {})
            handle = user.get("username") or "x-user"
            metrics = tweet.get("public_metrics", {})
            likes = int(metrics.get("like_count", 0) or 0)
            retweets = int(metrics.get("retweet_count", 0) or 0)
            replies = int(metrics.get("reply_count", 0) or 0)
            quotes = int(metrics.get("quote_count", 0) or 0)
            summary = (
                f"X 上的华语高热讨论，作者 @{handle}，"
                f"当前点赞 {likes}、转发 {retweets}、回复 {replies}、引用 {quotes}。"
            )
            if contains_excluded_terms(text, summary):
                continue
            category, matched_keywords, score, _ = score_text(
                text,
                f"{summary} {query}",
                source["id"],
                source.get("category_hint"),
            )
            metrics_score = (
                likes * 0.03
                + retweets * 0.06
                + replies * 0.04
                + quotes * 0.05
            )

            yield NewsItem(
                title=truncate_text(text, 78),
                summary=truncate_text(summary, 112),
                url=f"https://x.com/{handle}/status/{tweet.get('id')}",
                source_id=source["id"],
                source="X",
                source_url=source["url"],
                source_group=source.get("source_group", "community"),
                category=category,
                published=date_iso,
                published_display=date_display,
                matched_keywords=matched_keywords,
                score=score + metrics_score,
            )


def dedupe_and_sort(
    items: Iterable[NewsItem],
    timezone: ZoneInfo,
    source_settings: dict[str, dict],
) -> list[NewsItem]:
    now = datetime.now(timezone)
    deduped: dict[str, NewsItem] = {}
    semantic_entries: list[tuple[set[str], str, NewsItem]] = []

    for item in items:
        key = normalize_title(item.title)
        if not key:
            continue

        item_dt = parse_date(item.published or "", timezone)
        max_age_days = source_settings.get(item.source_id, {}).get("max_age_days", 365)
        cutoff = now - timedelta(days=max_age_days)
        if item_dt is not None and item_dt < cutoff:
            continue

        existing = deduped.get(key)
        if existing is None or item.score > existing.score:
            deduped[key] = item

        candidate_fp = build_semantic_fingerprint(item.title, item.summary)
        replaced = False
        for idx, (existing_fp, _existing_key, existing_item) in enumerate(semantic_entries):
            # Same source + high overlap is typically duplicated rewrites of one story.
            if item.source_group != existing_item.source_group:
                continue
            if token_jaccard(candidate_fp, existing_fp) < 0.72:
                continue
            if item.score > existing_item.score:
                semantic_entries[idx] = (candidate_fp, key, item)
            replaced = True
            break
        if not replaced:
            semantic_entries.append((candidate_fp, key, item))

    def sort_key(item: NewsItem) -> tuple[float, datetime]:
        dt = parse_date(item.published or "", timezone) or datetime(2000, 1, 1, tzinfo=timezone)
        age_days = max(0, (now - dt).days)
        freshness_bonus = max(0.0, 45.0 - age_days) / 9.0
        return (item.score + freshness_bonus, dt)

    candidates = [entry[2] for entry in semantic_entries]
    return sorted(candidates, key=sort_key, reverse=True)


def build_source_health(config: dict, featured_items: list[NewsItem], fetch_failures: list[dict[str, str]]) -> dict:
    all_sources = [source.get("id") for source in config.get("sources", []) if source.get("id")]
    item_counter = Counter(item.source_id for item in featured_items)
    failure_counter = Counter(failure["source_id"] for failure in fetch_failures)
    status_by_source: dict[str, dict[str, int | str]] = {}

    for source_id in all_sources:
        picked = int(item_counter.get(source_id, 0))
        failures = int(failure_counter.get(source_id, 0))
        status = "ok" if failures == 0 else ("degraded" if picked > 0 else "failed")
        status_by_source[source_id] = {
            "status": status,
            "picked_items": picked,
            "failures": failures,
        }

    return {
        "fetched_at": datetime.now(ZoneInfo(config.get("timezone", "Asia/Shanghai"))).isoformat(),
        "failed_sources": fetch_failures,
        "by_source": status_by_source,
    }


def build_ops_hints(featured_items: list[NewsItem]) -> list[str]:
    category_counter = Counter(item.category for item in featured_items)
    source_group_counter = Counter(item.source_group for item in featured_items)
    hints: list[str] = []

    if category_counter:
        top_category, top_count = category_counter.most_common(1)[0]
        hints.append(f"明日优先延展「{top_category}」相关选题（当前占比 {top_count}/{len(featured_items)}）。")
    if source_group_counter.get("community", 0) < 2:
        hints.append("社区类信号偏少，建议明日增加社区热议切口以提升互动。")
    if source_group_counter.get("news", 0) < 2:
        hints.append("媒体新闻信号偏少，建议补充权威媒体来源以稳定可信度。")
    if not hints:
        hints.append("当前来源与类别分布较均衡，明日可围绕高互动题材做角度微创新。")
    return hints


def select_featured_items(items: list[NewsItem], limit: int = 8) -> list[NewsItem]:
    chosen: list[NewsItem] = []
    seen: set[str] = set()

    def add_from(pool: Iterable[NewsItem], count: int) -> None:
        for item in pool:
            if len(chosen) >= limit or count <= 0:
                return
            key = normalize_title(item.title)
            if key in seen:
                continue
            seen.add(key)
            chosen.append(item)
            count -= 1

    add_from((i for i in items if i.source_id == "youtube_search"), 1)
    add_from((i for i in items if i.source_id == "x_recent_search"), 1)
    add_from((i for i in items if i.source_id == "reddit_search"), 1)
    add_from((i for i in items if i.source_group == "community"), 1)
    add_from((i for i in items if i.source_group == "news"), 3)
    add_from((i for i in items if i.category in {"命理新闻", "八字紫微"}), 2)
    add_from(items, limit - len(chosen))
    return chosen[:limit]


def select_home_items(items: list[NewsItem], timezone: ZoneInfo, limit: int = 3) -> list[NewsItem]:
    now = datetime.now(timezone)
    recent_items = []
    for item in items:
        item_dt = parse_date(item.published or "", timezone)
        if item_dt is None:
            continue
        if (now - item_dt).days <= 10:
            recent_items.append(item)
    pool = recent_items if recent_items else items
    return pool[:limit]


def render_home_teasers(items: list[NewsItem]) -> str:
    lines = ['                    <ul class="space-y-3 text-sm md:text-base text-gray-300">']
    for item in items[:3]:
        meta = f"{item.source} · {item.published_display}"
        lines.append(
            "                        <li class=\"flex items-start gap-3\">"
            "<span class=\"mt-1.5 h-2 w-2 shrink-0 rounded-full bg-cyan-300/80\"></span>"
            "<span>"
            f"{html.escape(item.title)}"
            f"<span class=\"ml-2 text-xs text-cyan-200/70\">{html.escape(meta)}</span>"
            "</span></li>"
        )
    lines.append("                    </ul>")
    return "\n".join(lines)


def render_stream_items(items: list[NewsItem]) -> str:
    cards: list[str] = []
    today_iso = datetime.utcnow().strftime("%Y-%m-%d")
    for item in items[:8]:
        date_iso = item.published or today_iso
        keyword_lines = "\n".join(
            f"                            <span>{html.escape(keyword)}</span>"
            for keyword in item.matched_keywords[:3]
        )
        cards.append(
            "\n".join(
                [
                    "                    <article class=\"stream-card\" itemscope itemtype=\"https://schema.org/Article\">",
                    "                        <div class=\"meta-line\">",
                    f"                            <span class=\"tag\">{html.escape(item.category)}</span>",
                    f"                            <span itemprop=\"datePublished\" content=\"{html.escape(date_iso)}\">{html.escape(item.published_display)}</span>",
                    f"                            <span>{html.escape(item.source)}</span>",
                    "                        </div>",
                    f"                        <h3 itemprop=\"headline\">{html.escape(item.title)}</h3>",
                    f"                        <p itemprop=\"description\">{html.escape(item.summary)}</p>",
                    "                        <div class=\"keyword-row\">",
                    keyword_lines,
                    "                        </div>",
                    f"                        <a class=\"inline-link\" href=\"{html.escape(item.url)}\" target=\"_blank\" rel=\"noopener noreferrer\">查看原文</a>",
                    "                    </article>",
                ]
            )
        )
    return "\n".join(cards)


def replace_between_markers(content: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = content.index(start_marker) + len(start_marker)
    end = content.index(end_marker)
    return content[:start] + "\n" + replacement + "\n                    " + content[end:]


def update_page_dates(content: str, date_display: str, date_iso: str) -> str:
    content = re.sub(
        r'(<span id="hot-news-updated">)最近更新：.*?(</span>)',
        rf"\1最近更新：{date_display}\2",
        content,
        count=1,
    )
    content = re.sub(
        r'(<span id="hot-news-feature-date" itemprop="dateModified" content=")([^"]+)(">)更新于 .*?(</span>)',
        lambda match: f'{match.group(1)}{date_iso}{match.group(3)}更新于 {date_display}{match.group(4)}',
        content,
        count=1,
    )
    content = re.sub(
        r'("dateModified": ")[^"]+(")',
        lambda match: f'{match.group(1)}{date_iso}{match.group(2)}',
        content,
        count=1,
    )
    return content


def update_sitemap(date_iso: str) -> None:
    content = SITEMAP_PATH.read_text(encoding="utf-8")
    content = re.sub(
        r"(<lastmod>)[^<]+(</lastmod>)",
        lambda match: f"{match.group(1)}{date_iso}{match.group(2)}",
        content,
    )
    SITEMAP_PATH.write_text(content, encoding="utf-8")


def write_data(
    items: list[NewsItem],
    date_display: str,
    date_iso: str,
    config: dict,
    source_health: dict,
    ops_hints: list[str],
) -> None:
    payload = {
        "updated_at": date_iso,
        "updated_at_display": date_display,
        "sources": config["sources"],
        "source_health": source_health,
        "ops_hints": ops_hints,
        "items": [asdict(item) for item in items],
    }
    DATA_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def collect_from_source(source: dict, timezone: ZoneInfo) -> list[NewsItem]:
    source_type = source.get("type")
    if source_type == "google_news_rss":
        return list(parse_google_news_rss(source, timezone))
    if source_type == "ptt_search":
        return list(parse_ptt_search(source, timezone))
    if source_type == "youtube_search":
        return list(parse_youtube_search(source, timezone))
    if source_type == "x_recent_search":
        return list(parse_x_recent_search(source, timezone))
    if source_type == "reddit_search":
        return list(parse_reddit_search(source, timezone))
    if source_type == "watch_urls":
        return []
    raise RuntimeError(f"unsupported source type: {source_type}")


def main() -> None:
    load_env_files()
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    timezone = ZoneInfo(config.get("timezone", "Asia/Shanghai"))
    source_settings = {source["id"]: source for source in config["sources"]}
    collected: list[NewsItem] = []
    fetch_failures: list[dict[str, str]] = []

    for source in config["sources"]:
        try:
            collected.extend(collect_from_source(source, timezone))
        except Exception as exc:
            fetch_failures.append({"source_id": source["id"], "name": source.get("name", source["id"]), "error": str(exc)})
            print(f"[warn] failed to fetch {source['name']}: {exc}")

    items = dedupe_and_sort(collected, timezone, source_settings)
    if len(items) < 6:
        for fallback in FALLBACK_ITEMS:
            items.append(NewsItem(**fallback))
    featured_items = select_featured_items(items)
    home_items = select_home_items(items, timezone)

    now = datetime.now(timezone)
    date_iso = now.strftime("%Y-%m-%d")
    date_display = f"{now.year}年{now.month}月{now.day}日 {now:%H:%M}"
    source_health = build_source_health(config, featured_items, fetch_failures)
    ops_hints = build_ops_hints(featured_items)

    write_data(featured_items, date_display, date_iso, config, source_health, ops_hints)

    page = PAGE_PATH.read_text(encoding="utf-8")
    page = replace_between_markers(
        page,
        "<!-- HOT_NEWS_STREAM_START -->",
        "<!-- HOT_NEWS_STREAM_END -->",
        render_stream_items(featured_items),
    )
    page = update_page_dates(page, date_display, date_iso)
    PAGE_PATH.write_text(page, encoding="utf-8")

    index = INDEX_PATH.read_text(encoding="utf-8")
    index = replace_between_markers(
        index,
        "<!-- HOT_NEWS_HOME_START -->",
        "<!-- HOT_NEWS_HOME_END -->",
        render_home_teasers(home_items),
    )
    INDEX_PATH.write_text(index, encoding="utf-8")

    update_sitemap(date_iso)
    print(f"updated {len(featured_items)} hot news items at {date_display}")


if __name__ == "__main__":
    main()
