import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

PERFORMANCE_FILE = "performance.json"


def get_token(client):
    response = client.post("/token", data={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.fixture(autouse=True)
def cleanup_performance():
    # Remove performance.json before each test
    if os.path.exists(PERFORMANCE_FILE):
        os.remove(PERFORMANCE_FILE)
    yield
    if os.path.exists(PERFORMANCE_FILE):
        os.remove(PERFORMANCE_FILE)


def test_add_and_get_performance():
    client = TestClient(app)
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    trade_payload = {
        "pnl": 120.5,
        "risk": 0.35,
        "drawdown": -0.08,
        "notes": "Test trade entry.",
    }
    # Add trade
    response = client.post(
        "/analytics/performance", json=trade_payload, headers=headers
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "saved"
    # Get performance
    get_response = client.get("/analytics/performance", headers=headers)
    assert get_response.status_code == 200
    perf = get_response.json()
    assert perf["total_trades"] == 1
    assert perf["total_pnl"] == 120.5
    assert perf["avg_pnl"] == 120.5
    assert perf["avg_risk"] == 0.35
    assert perf["max_drawdown"] == -0.08
    assert len(perf["trades"]) == 1
    assert perf["trades"][0]["notes"] == "Test trade entry."


def test_performance_requires_auth():
    client = TestClient(app)
    trade_payload = {
        "pnl": 120.5,
        "risk": 0.35,
        "drawdown": -0.08,
        "notes": "Test trade entry.",
    }
    response = client.post("/analytics/performance", json=trade_payload)
    assert response.status_code == 401
    get_response = client.get("/analytics/performance")
    assert get_response.status_code == 401
