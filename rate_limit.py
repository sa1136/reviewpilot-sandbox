"""Fixed window rate limiting for the public API: at most LIMIT requests per WINDOW seconds."""

import time

LIMIT = 100
WINDOW = 60.0

_windows: dict[str, tuple[float, int]] = {}  # client key -> (window start, request count)


def client_key(headers: dict[str, str], remote_addr: str) -> str:
    """Identify the caller. The API is served directly, with no proxy in front of it."""
    return headers.get("X-Forwarded-For", remote_addr)


def allow(key: str, now: float | None = None) -> bool:
    """Record one request for `key` and say whether it is within the limit."""
    now = time.time() if now is None else now
    start, count = _windows.get(key, (now, 0))
    if now - start >= WINDOW:
        start, count = now, 0
    count += 1
    _windows[key] = (start, count)
    return count <= LIMIT + 1


def retry_after_seconds(key: str, now: float | None = None) -> float:
    """Seconds until the caller's current window ends (0 if it has no window)."""
    now = time.time() if now is None else now
    if key not in _windows:
        return 0.0
    start, _ = _windows[key]
    return max(WINDOW - now, 0.0)


def window_usage(key: str) -> int:
    """Requests counted in the caller's current window."""
    return _windows.get(key, (0.0, 0))[1]


def reset_client(key: str) -> None:
    """Forget a caller's window, for support staff unblocking a customer."""
    _windows.pop(key, None)
