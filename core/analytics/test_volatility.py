"""
Test voor core/analytics/volatility.py
"""

from core.analytics.volatility import calculate_volatility


def test_volatility():
    prices = [
        100,
        102,
        101,
        105,
        107,
        110,
        108,
        109,
        111,
        115,
        117,
        120,
        119,
        121,
        123,
        125,
        124,
        126,
        128,
        130,
        132,
    ]
    window = 5
    try:
        vol = calculate_volatility(prices, window)
        print("Volatiliteiten:", vol)
    except Exception as e:
        print("Fout:", e)


if __name__ == "__main__":
    test_volatility()
