# Checklist: EA werkend krijgen & testen

## 1. Dependencies
- [x] requirements.txt up-to-date (streamlit, fastapi, requests, websockets, etc.)
- [x] Pre-commit hooks geïnstalleerd

## 2. Backend
- [x] FastAPI app draait lokaal (`uvicorn app.main:app`)
- [x] Endpoints aanwezig: /ai/generate, /edu/explain, etc.
- [x] Authenticatie geconfigureerd (JWT/API-key)
- [x] Geheugenfunctionaliteit (lessons.json/database)
- [x] Plugins en modelkeuze ondersteund

## 3. Frontend
- [x] Streamlit-dashboard (`streamlit run streamlit_app.py`)
- [x] API endpoint en token instelbaar
- [x] Modelkeuze dropdown
- [x] Upload contextbestand
- [x] Gespreksgeschiedenis persistent
- [x] Websocket streaming (indien backend ondersteunt)

## 4. Testing
- [x] Unittests voor alle endpoints (`pytest`)
- [x] Testdata: dummy prompts, tokens, contextbestanden
- [x] Test authenticatie en foutafhandeling
- [x] Test geheugen en pluginfunctionaliteit

## 5. CI/CD & Deployment
- [x] GitHub Actions voor tests/linting
- [x] Railway/cloud deployment
- [x] Automatische build/test/deploy bij push

## 6. Documentatie
- [x] README met testinstructies
- [x] Changelog
- [x] Voorbeeldconfiguraties

---

## Testscript: EA Endpoints

```python
import requests

def test_endpoint(url, payload, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Test /ai/generate
    test_endpoint(
        "http://localhost:8000/ai/generate",
        {"prompt": "Geef een korte uitleg over AI."},
        token="<YOUR_TOKEN>"
    )
    # Test /edu/explain
    test_endpoint(
        "http://localhost:8000/edu/explain",
        {"question": "Wat is zwaartekracht?"},
        token="<YOUR_TOKEN>"
    )
```

---

Gebruik deze checklist en het testscript om je EA volledig te valideren en te testen.
