import os

import pytest
from fastapi.testclient import TestClient

from app.main import app


def get_token(client):
    response = client.post("/token", data={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.fixture(autouse=True)
def cleanup_lessons():
    # Remove lessons.json before each test
    if os.path.exists("lessons.json"):
        os.remove("lessons.json")
    yield
    if os.path.exists("lessons.json"):
        os.remove("lessons.json")


def test_add_and_get_feedback():
    client = TestClient(app)
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    feedback_payload = {"user": "admin", "feedback": "Test feedback entry."}
    # Add feedback
    response = client.post("/ai/feedback", json=feedback_payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "saved"
    assert data["entry"]["user"] == "admin"
    assert data["entry"]["feedback"] == "Test feedback entry."
    # Get feedback
    get_response = client.get("/ai/feedback", headers=headers)
    assert get_response.status_code == 200
    feedback_list = get_response.json()
    assert isinstance(feedback_list, list)
    assert feedback_list[0]["user"] == "admin"
    assert feedback_list[0]["feedback"] == "Test feedback entry."


def test_feedback_requires_auth():
    client = TestClient(app)
    feedback_payload = {"user": "admin", "feedback": "Test feedback entry."}
    response = client.post("/ai/feedback", json=feedback_payload)
    assert response.status_code == 401
    get_response = client.get("/ai/feedback")
    assert get_response.status_code == 401
