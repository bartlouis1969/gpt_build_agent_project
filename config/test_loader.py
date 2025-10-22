"""
Test voor config/loader.py
"""


import unittest
from loader import load_config


class TestConfigLoader(unittest.TestCase):
    def test_load_config_valid(self):
        config = load_config()
        self.assertIsInstance(config, dict)

    def test_config_has_required_keys(self):
        config = load_config()
        required_keys = ["ENV", "LOGGING", "SECURITY"]
        for key in required_keys:
            self.assertIn(key, config)

    def test_get_openai_api_key(self):
        from loader import get_openai_api_key

        key = get_openai_api_key()
        self.assertTrue(key.startswith("sk-"))

    def test_get_model_name(self):
        from loader import get_model_name

        model = get_model_name()
        self.assertIsInstance(model, str)
        self.assertTrue(len(model) > 0)

    def test_get_default_temperature(self):
        from loader import get_default_temperature

        temp = get_default_temperature()
        self.assertTrue(0.0 <= temp <= 1.0)

    def test_get_max_tokens(self):
        from loader import get_max_tokens

        tokens = get_max_tokens()
        self.assertTrue(0 < tokens <= 4000)

    def test_get_gpt_timeout(self):
        from loader import get_gpt_timeout

        timeout = get_gpt_timeout()
        self.assertTrue(5 <= timeout <= 120)


if __name__ == "__main__":
    unittest.main()
