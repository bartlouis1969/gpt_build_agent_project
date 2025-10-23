import requests
from datetime import datetime

# Haal een JWT-token op
TOKEN_URL = "http://localhost:8000/token"
LOGIN_DATA = {"username": "admin", "password": "admin"}
response = requests.post(TOKEN_URL, data=LOGIN_DATA)
token = response.json()["access_token"]
print("JWT token:", token)

# Voeg een trade toe
PERF_URL = "http://localhost:8000/analytics/performance"
headers = {"Authorization": f"Bearer {token}"}
trade_payload = {
    "timestamp": datetime.utcnow().isoformat(),
    "pnl": 120.5,
    "risk": 0.35,
    "drawdown": -0.08,
    "notes": "Test trade entry.",
}
add_response = requests.post(PERF_URL, json=trade_payload, headers=headers)
print("Add trade status:", add_response.status_code)
print("Add trade response:", add_response.json())

# Haal alle performance KPIs op
get_response = requests.get(PERF_URL, headers=headers)
print("Performance KPIs:", get_response.json())
