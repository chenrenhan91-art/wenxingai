#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
BUFFER_REST_BASE_URL = "https://api.bufferapp.com/1"


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


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "WenxingAI/1.0 (+https://wenxingai.top)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    load_env_files()
    api_key = os.getenv("BUFFER_API_KEY", "").strip()
    if not api_key:
        raise SystemExit("missing BUFFER_API_KEY")

    url = f"{BUFFER_REST_BASE_URL}/profiles.json?access_token={urllib.parse.quote(api_key)}"
    profiles = fetch_json(url)
    if not isinstance(profiles, list):
        raise SystemExit("unexpected Buffer profiles response")

    service_to_env = {
        "threads": "BUFFER_THREADS_PROFILE_ID",
        "twitter": "BUFFER_X_PROFILE_ID",
        "x": "BUFFER_X_PROFILE_ID",
        "instagram": "BUFFER_INSTAGRAM_PROFILE_ID",
        "facebook": "BUFFER_FACEBOOK_PROFILE_ID",
    }
    suggestions: dict[str, list[dict[str, str]]] = {}

    print("Buffer profiles:")
    for profile in profiles:
        service = str(profile.get("service", ""))
        profile_id = str(profile.get("id", ""))
        username = str(profile.get("formatted_username") or profile.get("service_username") or "")
        timezone = str(profile.get("timezone", ""))
        print(f"- service={service} | id={profile_id} | account={username} | timezone={timezone}")
        env_name = service_to_env.get(service)
        if env_name:
            suggestions.setdefault(env_name, []).append(
                {"id": profile_id, "account": username, "service": service}
            )

    print("\nSuggested env mappings:")
    for env_name, entries in suggestions.items():
        if len(entries) == 1:
            print(f"- {env_name}={entries[0]['id']}  # {entries[0]['service']} {entries[0]['account']}")
        else:
            print(f"- {env_name}=<choose one>")
            for entry in entries:
                print(f"  - {entry['id']}  # {entry['service']} {entry['account']}")


if __name__ == "__main__":
    main()
