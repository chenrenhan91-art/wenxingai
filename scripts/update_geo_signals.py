#!/usr/bin/env python3
"""
Daily GEO freshness signal updater.
Updates article:modified_time, dateModified (JSON-LD), and sitemap lastmod
across all site pages. Run every day in GitHub Actions.
"""

import re
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
TODAY_ISO = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

HTML_PAGES = [
    "index.html",
    "mingli-xuanxue-news.html",
    "geo-answers.html",
    "glossary.html",
]


def update_html(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    original = text

    # <meta name="article:modified_time" content="...">
    text = re.sub(
        r'(<meta\s+name="article:modified_time"\s+content=")[^"]*(")',
        rf'\g<1>{TODAY_ISO}\g<2>',
        text,
    )
    # "dateModified": "..." in JSON-LD
    text = re.sub(
        r'("dateModified"\s*:\s*")[^"]*(")',
        rf'\g<1>{TODAY}\g<2>',
        text,
    )

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"  freshness updated: {path.name}")
        return True
    print(f"  no change: {path.name}")
    return False


def update_sitemap(path: Path) -> None:
    if not path.exists():
        print(f"  sitemap not found: {path}")
        return
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", f"<lastmod>{TODAY}</lastmod>", text)
    path.write_text(text, encoding="utf-8")
    print(f"  sitemap lastmod → {TODAY}")


if __name__ == "__main__":
    print(f"[update_geo_signals] date={TODAY}")
    for name in HTML_PAGES:
        update_html(BASE / name)
    update_sitemap(BASE / "sitemap.xml")
    print("[update_geo_signals] done")
