from __future__ import annotations

import csv
import os
from datetime import UTC, datetime
from pathlib import Path

import pytest
import requests

pytestmark = pytest.mark.integration

BASE = os.getenv("APP_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
TOKEN_URL = f"{BASE}/token"
FEEDBACK_URL = f"{BASE}/ai/feedback"
LOGIN_DATA = {"username": "admin", "password": "admin"}
API_URL = f"{BASE}/ai/generate"
PERF_URL = f"{BASE}/analytics/performance"
PLUGIN_URL = f"{BASE}/plugin/time"


"""
credits_manager.py

Beheer credits per gebruiker. Logt transacties naar CSV. Voorbeeldgebruik:

    from credits_manager import CreditsManager
    cm = CreditsManager('credits_log.csv')
    cm.add_user('alice', 100)
    cm.earn_credits('alice', 50)
    cm.spend_credits('alice', 20)
    print(cm.get_balance('alice'))
"""


class CreditsManager:
    """Beheer credits en log transacties naar CSV (append-only, idempotent)."""

    def __init__(self, log_file: str) -> None:
        self.log_file: str = log_file
        self.users: dict[str, float] = {}
        self._load()

    def _load(self) -> None:
        if not os.path.exists(self.log_file):
            return
        with open(self.log_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                user = row["user"]
                credits = float(row["balance"])
                self.users[user] = credits

    def add_user(self, user: str, initial_credits: float = 0) -> None:
        if user not in self.users:
            self.users[user] = initial_credits
            self._log(user, "init", initial_credits)

    def earn_credits(self, user: str, amount: float) -> None:
        self._ensure_user(user)
        self.users[user] += amount
        self._log(user, "earn", amount)

    def spend_credits(self, user: str, amount: float) -> None:
        self._ensure_user(user)
        if self.users[user] < amount:
            raise ValueError("Insufficient credits")
        self.users[user] -= amount
        self._log(user, "spend", -amount)

    def get_balance(self, user: str) -> float:
        self._ensure_user(user)
        return self.users[user]

    def _ensure_user(self, user: str) -> None:
        if user not in self.users:
            self.add_user(user, 0)

    def _log(self, user: str, action: str, amount: float) -> None:
        # Idempotent logging: check last entry for user/action/amount before writing
        log_path = Path(self.log_file)
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "user": user,
            "action": action,
            "amount": amount,
            "balance": self.users[user],
        }
        write_header = not log_path.exists() or log_path.stat().st_size == 0
        # Only append if not duplicate (last line)
        should_write = True
        if log_path.exists():
            with open(log_path, encoding="utf-8") as f:
                lines = f.readlines()
                if lines:
                    last = lines[-1].strip().split(",")
                    if len(last) == 5:  # noqa: SIM102
                        if (
                            last[1] == user
                            and last[2] == action
                            and float(last[3]) == amount
                            and float(last[4]) == self.users[user]
                        ):
                            should_write = False
        if should_write:
            with open(log_path, "a", newline="", encoding="utf-8") as f:
                fieldnames = ["timestamp", "user", "action", "amount", "balance"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if write_header:
                    writer.writeheader()
                writer.writerow(entry)


def test_feedback_flow_reachable():
    try:
        r = requests.post(TOKEN_URL, data=LOGIN_DATA, timeout=3)
        token = r.json().get("access_token", "")
        headers = {"Authorization": f"Bearer {token}"}
        feedback_payload = {
            "user": "admin",
            "feedback": "De AI-strategie werkt goed, maar kan sneller reageren op volatiliteit.",
            "timestamp": datetime.utcnow().isoformat(),
        }
        feedback_response = requests.post(
            FEEDBACK_URL, json=feedback_payload, headers=headers, timeout=3
        )
    except Exception:
        pytest.skip("Skipping: API server not running on 127.0.0.1:8000")
    assert r.status_code in (200, 401)
    assert feedback_response.status_code in (200, 401)


def test_jwt_token_flow():
    try:
        r = requests.post(TOKEN_URL, data=LOGIN_DATA, timeout=3)
        token = r.json().get("access_token", "")
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"prompt": "Geef drie tradingstrategie  n voor een volatiele markt"}
        api_response = requests.post(API_URL, json=payload, headers=headers, timeout=3)
    except Exception:
        pytest.skip("Skipping: API server not running on 127.0.0.1:8000")
    assert r.status_code in (200, 401)
    assert api_response.status_code in (200, 401)


def test_performance_flow_reachable():
    try:
        r = requests.post(TOKEN_URL, data=LOGIN_DATA, timeout=3)
        token = r.json().get("access_token", "")
        headers = {"Authorization": f"Bearer {token}"}
        trade_payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "pnl": 120.5,
            "risk": 0.35,
            "drawdown": -0.08,
            "notes": "Test trade entry.",
        }
        add_response = requests.post(PERF_URL, json=trade_payload, headers=headers, timeout=3)
    except Exception:
        pytest.skip("Skipping: API server not running on 127.0.0.1:8000")
    assert r.status_code in (200, 401)
    assert add_response.status_code in (200, 401)


def test_plugin_time_reachable():
    try:
        r = requests.post(TOKEN_URL, data=LOGIN_DATA, timeout=3)
        token = r.json().get("access_token", "")
        headers = {"Authorization": f"Bearer {token}"}
        plugin_response = requests.get(PLUGIN_URL, headers=headers, timeout=3)
    except Exception:
        pytest.skip("Skipping: API server not running on 127.0.0.1:8000")
    assert r.status_code in (200, 401)
    assert plugin_response.status_code in (200, 401)
