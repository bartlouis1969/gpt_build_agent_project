from fastapi import APIRouter
from core.analytics.signal_check_models import (
    SignalCheckRequest,
    SignalCheckResponse,
    SignalCheckDetails,
)

router = APIRouter()


@router.post("/analytics/signal-check", response_model=SignalCheckResponse)
def signal_check(request: SignalCheckRequest) -> SignalCheckResponse:
    import numpy as np

    signals = np.array(request.signal)
    prices = np.array(request.prices)
    trades_executed = int(np.sum(signals != 0))

    # Simuleer eenvoudige strategie: koop bij 1, verkoop bij -1
    returns_list = []
    position = 0
    entry_price = 0.0
    for s, p in zip(signals, prices):
        if s == 1 and position == 0:
            position = 1
            entry_price = float(p)
        elif s == -1 and position == 1:
            returns_list.append(float((float(p) - entry_price) / entry_price))
            position = 0
    if position == 1:
        returns_list.append(float((float(prices[-1]) - entry_price) / entry_price))
    returns = (
        np.array(returns_list, dtype=float)
        if returns_list
        else np.array([0.0], dtype=float)
    )

    # Score: gemiddelde rendement
    score = float(np.mean(returns))
    # Risico: standaarddeviatie van rendementen
    risk = float(np.std(returns))
    # Volatiliteit: standaarddeviatie van prijsveranderingen
    volatility = float(np.std(np.diff(prices)))
    # Sharpe ratio: gemiddeld rendement / risico
    sharpe_ratio = float(score / risk) if risk != 0 else 0.0
    # Max drawdown: grootste daling vanaf piek
    cum_returns = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(cum_returns)
    drawdown = (cum_returns - peak) / peak
    max_drawdown = float(np.min(drawdown)) if len(drawdown) > 0 else 0.0

    details = SignalCheckDetails(
        trades_executed=trades_executed,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown,
    )
    return SignalCheckResponse(
        score=score, risk=risk, volatility=volatility, details=details
    )
