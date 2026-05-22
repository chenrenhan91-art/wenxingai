#!/usr/bin/env python3
"""Create the public IndexNow key file from GitHub Actions configuration."""

from __future__ import annotations

import os
from pathlib import Path

from indexnow_key_file import DEFAULT_HOST, resolve_indexnow_key_file


ROOT = Path(__file__).resolve().parent.parent


def append_github_env(name: str, value: str) -> None:
    github_env = os.getenv("GITHUB_ENV", "").strip()
    if not github_env:
        return
    with open(github_env, "a", encoding="utf-8") as env_file:
        env_file.write(f"{name}={value}\n")


def main() -> None:
    key = os.getenv("INDEXNOW_KEY", "").strip()
    if not key:
        print("IndexNow key file skipped: INDEXNOW_KEY not configured")
        return

    host = os.getenv("INDEXNOW_HOST", DEFAULT_HOST).strip() or DEFAULT_HOST
    configured_location = os.getenv("INDEXNOW_KEY_LOCATION", "").strip()
    key_location, relative_path = resolve_indexnow_key_file(key, host, configured_location)
    target_path = (ROOT / relative_path).resolve()

    if ROOT.resolve() not in target_path.parents:
        raise SystemExit(f"Invalid IndexNow key path outside project: {relative_path}")

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(f"{key}\n", encoding="utf-8")

    append_github_env("INDEXNOW_KEY_LOCATION", key_location)
    append_github_env("INDEXNOW_KEY_FILE_PATH", relative_path)
    print(f"IndexNow key file ready: {relative_path}")
    print(f"IndexNow key location: {key_location}")


if __name__ == "__main__":
    main()