from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_signal_check_basic():
    payload = {
        "signal": [1, 0, 1, -1, 0],
        "prices": [100, 102, 101, 105, 103],
        "risk_level": "medium",
        "portfolio_value": 10000,
    }
    response = client.post("/analytics/signal-check", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "risk" in data
    assert "volatility" in data
    assert "details" in data
    assert data["details"]["trades_executed"] == 3
    assert isinstance(data["details"]["sharpe_ratio"], float)
    assert isinstance(data["details"]["max_drawdown"], float)
