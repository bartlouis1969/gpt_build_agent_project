from __future__ import annotations

import os

import pytest
import requests

pytestmark = pytest.mark.integration

BASE = os.getenv("APP_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
TOKEN_URL = f"{BASE}/token"
LOGIN_DATA = {"username": "test", "password": "test"}


def test_jwt_issuance_endpoint_up() -> None:
    try:
        r = requests.post(TOKEN_URL, data=LOGIN_DATA, timeout=3)
    except Exception:
        pytest.skip("API draait niet op 127.0.0.1:8000")
    assert r.status_code in (200, 401)
