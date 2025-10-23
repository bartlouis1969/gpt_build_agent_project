import requests
from datetime import datetime

# 1. Haal een JWT-token op
TOKEN_URL = "http://localhost:8000/token"
LOGIN_DATA = {"username": "admin", "password": "admin"}
response = requests.post(TOKEN_URL, data=LOGIN_DATA)
token = response.json()["access_token"]
print("JWT token:", token)

# 2. Stuur feedback naar /ai/feedback
FEEDBACK_URL = "http://localhost:8000/ai/feedback"
headers = {"Authorization": f"Bearer {token}"}
feedback_payload = {
    "user": "admin",
    "feedback": (
        "De AI-strategie werkt goed, " "maar kan sneller reageren op volatiliteit."
    ),
    "timestamp": datetime.utcnow().isoformat(),
}
feedback_response = requests.post(FEEDBACK_URL, json=feedback_payload, headers=headers)
print("Feedback status:", feedback_response.status_code)
print("Feedback response:", feedback_response.json())

# 3. Haal alle feedback op
get_response = requests.get(FEEDBACK_URL, headers=headers)
print("Alle feedback:", get_response.json())
