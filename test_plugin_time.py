from __future__ import annotations

import os

import pytest
import requests

pytestmark = pytest.mark.integration

BASE = os.getenv("APP_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
PLUGIN_URL = f"{BASE}/plugin/time"


def test_plugin_time_reachable() -> None:
    """Plugin/time route bereikbaar? 200/404 ok; anders skip."""
    try:
        r = requests.get(PLUGIN_URL, timeout=3)
    except Exception:
        pytest.skip("API draait niet op 127.0.0.1:8000")
    assert r.status_code in (200, 404)
