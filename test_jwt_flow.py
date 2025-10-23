import requests

# 1. Haal een JWT-token op
TOKEN_URL = "http://localhost:8000/token"
LOGIN_DATA = {"username": "admin", "password": "admin"}
response = requests.post(TOKEN_URL, data=LOGIN_DATA)
token = response.json()["access_token"]
print("JWT token:", token)

# 2. Gebruik het token voor een beveiligde API-call
API_URL = "http://localhost:8000/ai/generate"
payload = {"prompt": "Geef drie tradingstrategieën voor een volatiele markt"}
headers = {"Authorization": f"Bearer {token}"}
api_response = requests.post(API_URL, json=payload, headers=headers)
print("Status code:", api_response.status_code)
print("Response:", api_response.json())
