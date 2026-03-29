#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "generated"
BUNDLE_PATH = OUTPUT_DIR / "gemini-content-bundle.json"
SOCIAL_DIR = OUTPUT_DIR / "social-posts"
JOBS_PATH = OUTPUT_DIR / "distribution-jobs.json"
PACKAGE_PATH = OUTPUT_DIR / "distribution-package.md"
STATE_PATH = OUTPUT_DIR / "distribution-state.json"
DEFAULT_LANDING_URL = "https://karmaisacat.top/"
BUFFER_BASE_URL = "https://api.bufferapp.com/1"

DEFAULT_SCHEDULES = {
    "threads": "09:30",
    "x": "12:30",
    "facebook": "19:30",
    "instagram": "21:00",
}

PLATFORM_TO_SERVICE = {
    "threads": {"threads"},
    "x": {"twitter", "x"},
    "facebook": {"facebook"},
    "instagram": {"instagram"},
}

PLATFORM_TO_ENV = {
    "threads": "BUFFER_THREADS_PROFILE_ID",
    "x": "BUFFER_X_PROFILE_ID",
    "facebook": "BUFFER_FACEBOOK_PROFILE_ID",
    "instagram": "BUFFER_INSTAGRAM_PROFILE_ID",
}

PLATFORM_TO_BUNDLE_KEY = {
    "threads": "threads",
    "x": "x",
    "facebook": "facebook",
    "instagram": "instagram",
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


def fetch_json(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None) -> Any:
    req_headers = {"User-Agent": "WenxingAI/1.0 (+https://karmaisacat.top)"}
    if headers:
        req_headers.update(headers)
    request = urllib.request.Request(url, data=data, headers=req_headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_bundle() -> dict[str, Any]:
    if not BUNDLE_PATH.exists():
        raise RuntimeError("missing generated/gemini-content-bundle.json")
    return json.loads(BUNDLE_PATH.read_text(encoding="utf-8"))


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {"published": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict[str, Any]) -> None:
    write_json(STATE_PATH, state)


def normalize_landing_url(base_url: str, platform: str, slug: str) -> str:
    parsed = urllib.parse.urlparse(base_url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query.extend(
        [
            ("utm_source", platform),
            ("utm_medium", "social"),
            ("utm_campaign", slug),
        ]
    )
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query)))


def parse_time_string(value: str, fallback: str) -> tuple[int, int]:
    text = (value or "").strip()
    match = re.search(r"(\d{1,2}):(\d{2})", text)
    if not match:
        match = re.search(r"(\d{1,2})點(?:(\d{1,2})分)?", text)
    if not match:
        base_hour, base_minute = fallback.split(":")
        return int(base_hour), int(base_minute)

    hour = int(match.group(1))
    minute = int(match.group(2) or 0)
    lowered = text.lower()
    if any(token in lowered for token in ("下午", "晚上", "pm", "p.m")) and hour < 12:
        hour += 12
    if any(token in lowered for token in ("凌晨",)) and hour == 12:
        hour = 0
    return hour, minute


def ensure_future_schedule(base_dt: datetime, now: datetime, offset_minutes: int) -> datetime:
    candidate = base_dt + timedelta(minutes=offset_minutes)
    minimum = now + timedelta(minutes=10)
    if candidate <= minimum:
        candidate = minimum + timedelta(minutes=offset_minutes)
    rounded = candidate.replace(second=0, microsecond=0)
    minute_mod = rounded.minute % 5
    if minute_mod:
        rounded += timedelta(minutes=5 - minute_mod)
    return rounded


def build_post_text(platform: str, raw_text: str, landing_url: str) -> str:
    text = (raw_text or "").strip()
    if landing_url in text:
        return text
    if platform == "instagram":
        suffix = f"完整解讀與諮詢：{landing_url}"
    else:
        suffix = f"完整解讀：{landing_url}"
    return f"{text}\n\n{suffix}"


def build_jobs(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    timezone = ZoneInfo("Asia/Shanghai")
    now = datetime.now(timezone)
    source_date = bundle.get("source_snapshot_updated_at") or now.strftime("%Y-%m-%d")
    slug = bundle.get("slug") or f"daily-hot-news-{source_date}"
    social_posts = bundle.get("social_posts") or {}
    distribution_plan = bundle.get("distribution_plan") or {}
    landing_base = (os.getenv("SOCIAL_LANDING_URL") or DEFAULT_LANDING_URL).strip() or DEFAULT_LANDING_URL
    schedule_date = datetime.strptime(source_date, "%Y-%m-%d").replace(tzinfo=timezone)

    jobs: list[dict[str, Any]] = []
    for platform, bundle_key in PLATFORM_TO_BUNDLE_KEY.items():
        posts = social_posts.get(bundle_key) or []
        if not isinstance(posts, list) or not posts:
            continue

        fallback_time = DEFAULT_SCHEDULES[platform]
        hour, minute = parse_time_string(str(distribution_plan.get(platform, "")), fallback_time)
        base_dt = schedule_date.replace(hour=hour, minute=minute, second=0, microsecond=0)

        for index, raw_text in enumerate(posts, start=1):
            landing_url = normalize_landing_url(landing_base, platform, slug)
            scheduled_at = ensure_future_schedule(base_dt, now, offset_minutes=(index - 1) * 90)
            text = build_post_text(platform, str(raw_text), landing_url)
            text_hash = hashlib.sha1(text.encode("utf-8")).hexdigest()
            jobs.append(
                {
                    "slug": slug,
                    "platform": platform,
                    "position": index,
                    "scheduled_at": scheduled_at.isoformat(),
                    "landing_url": landing_url,
                    "text": text,
                    "text_hash": text_hash,
                    "status": "ready",
                }
            )
    return jobs


def render_package(bundle: dict[str, Any], jobs: list[dict[str, Any]], results: list[dict[str, Any]]) -> str:
    lines = [
        f"# 问星AI 多平台分发包 {bundle.get('source_snapshot_updated_at', '')}",
        "",
        f"- 内容包：{bundle.get('slug', '')}",
        f"- LLM：{bundle.get('model', '')}",
        f"- 站外落地页：{os.getenv('SOCIAL_LANDING_URL') or DEFAULT_LANDING_URL}",
        "",
        "## 分发任务",
    ]
    for job in jobs:
        lines.append(
            f"- {job['platform']} #{job['position']} | {job['scheduled_at']} | {job['status']}"
        )
    lines.extend(["", "## 发布结果"])
    if not results:
        lines.append("- 当前未执行自动发布，或没有可记录结果。")
    else:
        for result in results:
            lines.append(
                f"- {result['platform']} #{result['position']} | {result['status']} | {result.get('message', '')}"
            )
    lines.append("")
    return "\n".join(lines)


def write_social_exports(jobs: list[dict[str, Any]]) -> None:
    SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
    by_platform: dict[str, list[dict[str, Any]]] = {}
    for job in jobs:
        by_platform.setdefault(job["platform"], []).append(job)

    for platform, items in by_platform.items():
        lines = [f"# {platform}"]
        for item in items:
            lines.extend(
                [
                    "",
                    f"## Post {item['position']}",
                    f"- Scheduled At: {item['scheduled_at']}",
                    f"- Landing URL: {item['landing_url']}",
                    "",
                    item["text"],
                ]
            )
        (SOCIAL_DIR / f"{platform}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def get_buffer_profiles(api_key: str) -> list[dict[str, Any]]:
    url = f"{BUFFER_BASE_URL}/profiles.json?access_token={urllib.parse.quote(api_key)}"
    data = fetch_json(url)
    return data if isinstance(data, list) else []


def resolve_profile_id(platform: str, profiles: list[dict[str, Any]]) -> tuple[str | None, str | None]:
    explicit_profile_id = os.getenv(PLATFORM_TO_ENV[platform], "").strip()
    if explicit_profile_id:
        return explicit_profile_id, None

    matched = [
        profile for profile in profiles
        if str(profile.get("service", "")).lower() in PLATFORM_TO_SERVICE[platform]
    ]
    if not matched:
        return None, f"no Buffer profile found for {platform}"
    if len(matched) > 1:
        return None, f"multiple Buffer profiles found for {platform}; set {PLATFORM_TO_ENV[platform]}"
    return str(matched[0].get("id") or ""), None


def create_buffer_update(api_key: str, profile_id: str, job: dict[str, Any]) -> dict[str, Any]:
    payload = urllib.parse.urlencode(
        [
            ("access_token", api_key),
            ("profile_ids[]", profile_id),
            ("text", job["text"]),
            ("scheduled_at", job["scheduled_at"]),
            ("shorten", "false"),
            ("attachment", "true"),
        ]
    ).encode("utf-8")
    response = fetch_json(
        f"{BUFFER_BASE_URL}/updates/create.json",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    if not isinstance(response, dict):
        raise RuntimeError("invalid Buffer create response")
    return response


def publish_jobs_to_buffer(jobs: list[dict[str, Any]], state: dict[str, Any]) -> list[dict[str, Any]]:
    api_key = os.getenv("BUFFER_API_KEY", "").strip()
    if not api_key:
        return []

    profiles = get_buffer_profiles(api_key)
    published = state.setdefault("published", {})
    results: list[dict[str, Any]] = []

    for job in jobs:
        slug_bucket = published.setdefault(job["slug"], {})
        state_key = f"{job['platform']}:{job['position']}"
        existing = slug_bucket.get(state_key)
        if existing and existing.get("text_hash") == job["text_hash"]:
            job["status"] = "already_published"
            results.append(
                {
                    "platform": job["platform"],
                    "position": job["position"],
                    "status": "already_published",
                    "message": existing.get("buffer_update_id", ""),
                }
            )
            continue

        profile_id, error = resolve_profile_id(job["platform"], profiles)
        if error:
            job["status"] = "skipped"
            results.append(
                {
                    "platform": job["platform"],
                    "position": job["position"],
                    "status": "skipped",
                    "message": error,
                }
            )
            continue

        response = create_buffer_update(api_key, profile_id, job)
        updates = response.get("updates") or []
        buffer_update_id = ""
        if updates and isinstance(updates, list):
            buffer_update_id = str(updates[0].get("id") or "")

        job["status"] = "queued"
        slug_bucket[state_key] = {
            "text_hash": job["text_hash"],
            "buffer_update_id": buffer_update_id,
            "scheduled_at": job["scheduled_at"],
            "profile_id": profile_id,
            "queued_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        }
        results.append(
            {
                "platform": job["platform"],
                "position": job["position"],
                "status": "queued",
                "message": buffer_update_id or "queued in Buffer",
            }
        )
    return results


def main() -> None:
    load_env_files()
    if not BUNDLE_PATH.exists():
        print("skipped distribution: missing generated/gemini-content-bundle.json")
        return

    bundle = load_bundle()
    jobs = build_jobs(bundle)
    write_social_exports(jobs)
    write_json(JOBS_PATH, jobs)

    state = load_state()
    results = publish_jobs_to_buffer(jobs, state)
    if results:
        save_state(state)
        write_json(JOBS_PATH, jobs)
    PACKAGE_PATH.write_text(render_package(bundle, jobs, results), encoding="utf-8")

    if os.getenv("BUFFER_API_KEY", "").strip():
        queued = len([result for result in results if result["status"] == "queued"])
        print(f"prepared {len(jobs)} distribution jobs; queued {queued} jobs to Buffer")
    else:
        print(f"prepared {len(jobs)} distribution jobs; skipped Buffer publishing: missing BUFFER_API_KEY")


if __name__ == "__main__":
    main()
