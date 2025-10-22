"""
core/analytics/volatility.py

Module voor het berekenen van historische volatiliteit van een tijdreeks.
"""

import numpy as np


def calculate_volatility(prices, window=20):
    """
    Bereken de rolling standaarddeviatie (volatiliteit)
    van een lijst met prijzen.
    :param prices: List of floats (prijzen)
    :param window: Rolling window size
    :return: List of volatilities
    """
    prices = np.array(prices)
    if len(prices) < window:
        raise ValueError("Te weinig data voor window.")
    returns = np.diff(prices) / prices[:-1]
    volatilities = [
        np.std(returns[max(0, i - window) : i + 1]) for i in range(len(returns))
    ]
    return volatilities
