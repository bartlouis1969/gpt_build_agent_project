from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ai_generate():
    payload = {"prompt": "Geef drie tradingstrategieën voor een volatiele markt"}
    response = client.post("/ai/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Verwacht dat de route een JSON met 'content' terugstuurt (stub uit core/ai/generator.py)
    assert "content" in data
    assert isinstance(data["content"], str)
    assert data["content"].strip()
