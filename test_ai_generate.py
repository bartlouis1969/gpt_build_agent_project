import requests

# Vul hier de juiste URL van je live FastAPI backend in


def test_ai_generate():
    # Pas aan naar je live endpoint indien nodig
    url = "http://localhost:8000/ai/generate"
    payload = {"prompt": ("Geef drie tradingstrategieën voor een volatiele markt")}
    response = requests.post(url, json=payload)
    print("Status code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    test_ai_generate()
