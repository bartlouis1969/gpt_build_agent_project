import requests

# Haal een JWT-token op
TOKEN_URL = "http://localhost:8000/token"
LOGIN_DATA = {"username": "admin", "password": "admin"}
response = requests.post(TOKEN_URL, data=LOGIN_DATA)
token = response.json()["access_token"]
print("JWT token:", token)

# Call de plugin endpoint /plugin/time
PLUGIN_URL = "http://localhost:8000/plugin/time"
headers = {"Authorization": f"Bearer {token}"}
plugin_response = requests.get(PLUGIN_URL, headers=headers)
print("Status code:", plugin_response.status_code)
print("Response:", plugin_response.json())
