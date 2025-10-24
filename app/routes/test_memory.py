import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestMemoryEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_set_and_get_memory(self):
        # Opslaan
        response = self.client.post("/ai/memory", json={"key": "foo", "value": "bar"})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["key"], "foo")
        self.assertEqual(data["value"], "bar")
        self.assertIn("timestamp", data)

        # Ophalen
        response = self.client.get("/ai/memory/foo")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["key"], "foo")
        self.assertEqual(data["value"], "bar")
        self.assertIn("timestamp", data)

    def test_get_all_memory(self):
        self.client.post("/ai/memory", json={"key": "a", "value": "1"})
        self.client.post("/ai/memory", json={"key": "b", "value": "2"})
        response = self.client.get("/ai/memory")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        keys = [entry["key"] for entry in data]
        self.assertIn("a", keys)
        self.assertIn("b", keys)

    def test_get_missing_key(self):
        response = self.client.get("/ai/memory/notfound")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Key not found")


if __name__ == "__main__":
    unittest.main()
