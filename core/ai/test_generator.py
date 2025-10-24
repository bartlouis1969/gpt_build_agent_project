from __future__ import annotations

import os
import unittest

from core.ai.generator import generate_content


@unittest.skipUnless(os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY ontbreekt; test wordt geskipt")
class TestGenerator(unittest.TestCase):
    def test_generate_content(self) -> None:
        prompt = "Geef drie alternatieve trading headlines voor een bullish markt."
        result = generate_content(prompt)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        if result is not None:
            self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()
