from __future__ import annotations

import os

import pytest
import requests

pytestmark = pytest.mark.integration

BASE = os.getenv("APP_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
PERF_URL = f"{BASE}/api/analytics/performance"


def test_perf_flow_reachable() -> None:
    """Performance endpoint bereikbaar? 200/401/404 ok; anders skip."""
    try:
        r = requests.get(PERF_URL, timeout=3)
    except Exception:
        pytest.skip("API draait niet op 127.0.0.1:8000")
    assert r.status_code in (200, 401, 404)
