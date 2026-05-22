#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import socket
import time
import urllib.request
from typing import Any
from urllib.error import HTTPError, URLError


DEFAULT_MODEL_FALLBACKS = (
    "qwen3.6-flash-2026-04-16",
    "qwen3.5-flash",
    "qwen3.5-35b-a3b",
    "qwen3.5-27b",
    "qwen3.5-122b-a10b",
    "deepseek-v4-flash",
)

FALLBACK_STATUS_CODES = {400, 403, 404, 408, 409, 429}
FATAL_ERROR_MARKERS = (
    "invalidapikey",
    "invalid api key",
    "incorrect api key",
    "unauthorized",
    "authentication",
)
FALLBACK_ERROR_MARKERS = (
    "allocationquota",
    "freetieronly",
    "quota",
    "rate limit",
    "too many requests",
    "model",
    "not found",
    "does not exist",
    "not exist",
    "not available",
    "unavailable",
    "not support",
    "unsupported",
    "accessdenied",
)


def split_model_list(value: str | None) -> list[str]:
    if not value:
        return []
    normalized = value.replace("\n", ",")
    return [item.strip() for item in normalized.split(",") if item.strip()]


def unique_models(models: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for model in models:
        if model in seen:
            continue
        seen.add(model)
        result.append(model)
    return result


def models_from_env(
    primary_env: str,
    fallback_env: str,
    default_model: str,
    default_fallbacks: tuple[str, ...] = DEFAULT_MODEL_FALLBACKS,
) -> list[str]:
    primary_model = os.getenv(primary_env, default_model).strip() or default_model
    configured_fallbacks = split_model_list(os.getenv(fallback_env))
    fallback_models = configured_fallbacks or list(default_fallbacks)
    return unique_models([primary_model, *fallback_models])


def read_http_error_body(exc: HTTPError) -> str:
    body = getattr(exc, "dashscope_body", "")
    if body:
        return str(body)
    try:
        body = exc.read().decode("utf-8", errors="replace")
    except Exception:
        body = str(exc)
    setattr(exc, "dashscope_body", body)
    return body


def summarize_error(exc: Exception) -> str:
    if isinstance(exc, HTTPError):
        body = read_http_error_body(exc).strip().replace("\n", " ")
        if len(body) > 180:
            body = body[:177] + "..."
        return f"HTTP {exc.code}: {body or exc.reason}"
    return str(exc)


def should_try_next_model(exc: Exception) -> bool:
    if not isinstance(exc, HTTPError):
        return False
    if exc.code == 401:
        return False

    body = read_http_error_body(exc).lower()
    if any(marker in body for marker in FATAL_ERROR_MARKERS):
        return False
    if exc.code == 429:
        return True
    if exc.code in FALLBACK_STATUS_CODES:
        return not body or any(marker in body for marker in FALLBACK_ERROR_MARKERS)
    return 500 <= exc.code < 600


def request_chat_completion(
    *,
    endpoint: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
    response_format: dict[str, str] | None,
    timeout_seconds: int,
    retry_attempts: int,
    user_agent: str,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if response_format:
        payload["response_format"] = response_format

    last_exc: Exception | None = None
    for attempt in range(1, retry_attempts + 1):
        request = urllib.request.Request(
            endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {api_key}",
                "User-Agent": user_agent,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            read_http_error_body(exc)
            last_exc = exc
            if 500 <= exc.code < 600 and attempt < retry_attempts:
                time.sleep(min(2 * attempt, 6))
                continue
            raise
        except (URLError, socket.timeout, TimeoutError) as exc:
            last_exc = exc
            if attempt >= retry_attempts:
                break
            time.sleep(min(2 * attempt, 6))

    assert last_exc is not None
    raise last_exc


def call_chat_completion_with_fallback(
    *,
    endpoint: str,
    api_key: str,
    models: list[str],
    messages: list[dict[str, str]],
    response_format: dict[str, str] | None,
    timeout_seconds: int,
    retry_attempts: int,
    user_agent: str,
) -> tuple[dict[str, Any], str]:
    if not models:
        raise RuntimeError("DashScope model list is empty")

    last_exc: Exception | None = None
    for index, model in enumerate(models):
        try:
            payload = request_chat_completion(
                endpoint=endpoint,
                api_key=api_key,
                model=model,
                messages=messages,
                response_format=response_format,
                timeout_seconds=timeout_seconds,
                retry_attempts=retry_attempts,
                user_agent=user_agent,
            )
            if index > 0:
                print(f"[ok] DashScope fallback model selected: {model}")
            return payload, model
        except (HTTPError, URLError, socket.timeout, TimeoutError) as exc:
            last_exc = exc
            has_next_model = index < len(models) - 1
            if has_next_model and should_try_next_model(exc):
                next_model = models[index + 1]
                print(
                    f"[warn] DashScope model {model} failed; "
                    f"trying {next_model}. Reason: {summarize_error(exc)}"
                )
                continue
            raise

    assert last_exc is not None
    raise last_exc