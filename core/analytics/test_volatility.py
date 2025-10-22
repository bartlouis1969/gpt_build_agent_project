"""
Test voor core/analytics/volatility.py
"""

from core.analytics.volatility import calculate_volatility


def test_volatility():
    prices = [
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
    ]
    window = 5
    try:
        vol = calculate_volatility(prices, window)
        print("Volatiliteiten:", vol)
    except Exception as e:
        print("Fout:", e)


if __name__ == "__main__":
    test_volatility()
