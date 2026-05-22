#!/usr/bin/env python3
"""Submit sitemap URLs to IndexNow when INDEXNOW_KEY is configured."""

from __future__ import annotations

import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from zoneinfo import ZoneInfo

from indexnow_key_file import resolve_indexnow_key_file


ROOT = Path(__file__).resolve().parent.parent
SITEMAP_PATH = ROOT / "sitemap.xml"
REPORT_JSON_PATH = ROOT / "generated" / "indexnow-report.json"
REPORT_MD_PATH = ROOT / "generated" / "indexnow-report.md"
TIMEZONE = ZoneInfo("Asia/Shanghai")
DEFAULT_ENDPOINT = "https://api.indexnow.org/indexnow"
DEFAULT_HOST = "wenxingai.top"


def sitemap_urls() -> list[str]:
    if not SITEMAP_PATH.exists():
        return []
    tree = ET.parse(SITEMAP_PATH)
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = [
        loc.text.strip()
        for loc in tree.findall(f".//{namespace}loc")
        if loc.text and loc.text.strip().startswith("https://")
    ]
    return sorted(set(urls))


def write_report(report: dict) -> None:
    REPORT_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        f"# IndexNow 提交报告 {report['ran_at_display']}",
        "",
        f"- 状态：{report['status']}",
        f"- URL 数：{report['url_count']}",
        f"- Endpoint：{report.get('endpoint', '')}",
        f"- 说明：{report.get('message', '')}",
        "",
    ]
    REPORT_MD_PATH.write_text("\n".join(lines), encoding="utf-8")


def submit(urls: list[str], key: str, key_location: str, host: str, endpoint: str) -> tuple[int, str]:
    payload = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls[:10000],
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def main() -> None:
    now = datetime.now(TIMEZONE)
    key = os.getenv("INDEXNOW_KEY", "").strip()
    host = os.getenv("INDEXNOW_HOST", DEFAULT_HOST).strip() or DEFAULT_HOST
    endpoint = os.getenv("INDEXNOW_ENDPOINT", DEFAULT_ENDPOINT).strip() or DEFAULT_ENDPOINT
    configured_key_location = os.getenv("INDEXNOW_KEY_LOCATION", "").strip()
    key_location = ""
    if key:
        key_location, _ = resolve_indexnow_key_file(key, host, configured_key_location)

    urls = sitemap_urls()
    report = {
        "ran_at": now.isoformat(),
        "ran_at_display": now.strftime("%Y-%m-%d %H:%M %Z"),
        "status": "skipped",
        "url_count": len(urls),
        "endpoint": endpoint,
        "message": "INDEXNOW_KEY not configured",
    }

    if not key:
        write_report(report)
        print("IndexNow skipped: INDEXNOW_KEY not configured")
        return
    if not urls:
        report.update({"status": "skipped", "message": "sitemap has no URLs"})
        write_report(report)
        print("IndexNow skipped: sitemap has no URLs")
        return

    try:
        status_code, body = submit(urls, key, key_location, host, endpoint)
        report.update(
            {
                "status": "ok" if 200 <= status_code < 300 else "warn",
                "status_code": status_code,
                "key_location": key_location,
                "message": body[:500] or "submitted",
            }
        )
        print(f"IndexNow submitted {len(urls)} URLs: HTTP {status_code}")
    except (HTTPError, URLError, TimeoutError) as exc:
        report.update({"status": "failed", "key_location": key_location, "message": str(exc)})
        print(f"IndexNow failed: {exc}")
    write_report(report)


if __name__ == "__main__":
    main()