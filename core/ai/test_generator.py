"""
Test voor core/ai/generator.py
"""

import sys
import os
import unittest
from core.ai.generator import generate_content

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class TestGenerator(unittest.TestCase):
    def test_generate_content(self):
        prompt = "Geef drie alternatieve trading headlines " "voor een bullish markt."
        try:
            result = generate_content(prompt)
            self.assertIsInstance(result, str)
        except Exception as e:
            self.fail(f"generate_content raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
