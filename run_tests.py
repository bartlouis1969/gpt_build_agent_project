# run_tests.py
import unittest
import sys


def run():
    print("🔍 Testen worden uitgevoerd...\n")
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir="tests", pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("\n✅ Alle tests geslaagd!")
        sys.exit(0)
    else:
        print("\n❌ Sommige tests zijn gefaald.")
        sys.exit(1)


if __name__ == "__main__":
    run()
