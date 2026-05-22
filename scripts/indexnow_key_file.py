#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_HOST = "wenxingai.top"
DEFAULT_KEY_FILE = "indexnow-key.txt"
SAFE_PATH_PATTERN = re.compile(r"^[A-Za-z0-9._/-]+\.txt$")


def normalize_host(host: str | None) -> str:
    value = (host or DEFAULT_HOST).strip()
    if value.startswith("http://") or value.startswith("https://"):
        parsed = urlparse(value)
        value = parsed.netloc or DEFAULT_HOST
    return value.strip("/") or DEFAULT_HOST


def safe_relative_txt_path(value: str, key: str) -> str:
    candidate = value.strip().lstrip("/")
    if candidate == key or not SAFE_PATH_PATTERN.match(candidate):
        return DEFAULT_KEY_FILE
    parts = Path(candidate).parts
    if any(part in {"", ".", ".."} for part in parts):
        return DEFAULT_KEY_FILE
    return candidate


def resolve_indexnow_key_file(
    key: str,
    host: str | None = None,
    configured_location: str | None = None,
) -> tuple[str, str]:
    normalized_host = normalize_host(host)
    location = (configured_location or "").strip()

    if location.startswith("http://") or location.startswith("https://"):
        parsed = urlparse(location)
        relative_path = safe_relative_txt_path(parsed.path, key)
        netloc = parsed.netloc or normalized_host
        return f"https://{netloc}/{relative_path}", relative_path

    if location:
        relative_path = safe_relative_txt_path(location, key)
        return f"https://{normalized_host}/{relative_path}", relative_path

    return f"https://{normalized_host}/{DEFAULT_KEY_FILE}", DEFAULT_KEY_FILE