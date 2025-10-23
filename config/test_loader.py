"""
Test voor config/loader.py
"""

import unittest
from config.loader import (
    get_openai_api_key,
    get_model_name,
    get_default_temperature,
    get_max_tokens,
    get_gpt_timeout,
)


class TestConfigLoader(unittest.TestCase):
    def test_get_openai_api_key(self):
        key = get_openai_api_key()
        self.assertTrue(key.startswith("sk-"))

    def test_get_model_name(self):
        model = get_model_name()
        self.assertIsInstance(model, str)
        self.assertTrue(len(model) > 0)

    def test_get_default_temperature(self):
        temp = get_default_temperature()
        self.assertTrue(0.0 <= temp <= 1.0)

    def test_get_max_tokens(self):
        tokens = get_max_tokens()
        self.assertTrue(0 < tokens <= 4000)

    def test_get_gpt_timeout(self):
        timeout = get_gpt_timeout()
        self.assertTrue(5 <= timeout <= 120)


if __name__ == "__main__":
    unittest.main()
