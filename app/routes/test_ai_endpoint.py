"""
Unittest voor POST /ai/generate endpoint in ai_generator.py
"""

import unittest
from fastapi.testclient import TestClient
from app.routes.ai_generator import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)


class TestAIGenerateEndpoint(unittest.TestCase):
    def test_generate_ai_content(self):
        client = TestClient(app)
        payload = {
            "prompt": "Geef een trading headline voor een bullmarkt.",
            "model": None,
            "temperature": 0.7,
            "max_tokens": 50,
        }
        response = client.post("/ai/generate", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("content", data)
        self.assertIsInstance(data["content"], str)


if __name__ == "__main__":
    unittest.main()
