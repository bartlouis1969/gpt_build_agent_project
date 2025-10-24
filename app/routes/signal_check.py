from __future__ import annotations

from typing import TypedDict

from fastapi import APIRouter
from pydantic import BaseModel


# TypedDicts for mypy/static typing
class SignalStats(TypedDict):
    n: int
    sharpe_ratio: float
    max_drawdown: float
    mean_return: float
    volatility: float
    trades_executed: int


class SignalResponse(TypedDict, total=False):
    score: float
    risk: float
    volatility: float
    sharpe_ratio: float
    max_drawdown: float
    details: SignalStats


router = APIRouter()


class SignalPayload(BaseModel):
    signal: list[float]
    prices: list[float]
    risk_level: str
    portfolio_value: float


def _pct_changes(vals: list[float]) -> list[float]:
    if len(vals) < 2:
        return []
    return [(vals[i] - vals[i - 1]) / vals[i - 1] for i in range(1, len(vals))]


def _mean(xs: list[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def _std(xs: list[float]) -> float:
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    var = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    return var**0.5


def _max_drawdown(vals: list[float]) -> float:
    peak = vals[0] if vals else 0.0
    mdd = 0.0
    for v in vals:
        if v > peak:
            peak = v
        drawdown = (peak - v) / peak if peak else 0.0
        if drawdown > mdd:
            mdd = drawdown
    return float(mdd)


@router.post("/signal-check")
def signal_check(payload: SignalPayload) -> SignalResponse:
    changes = _pct_changes(payload.prices)
    vol = _std(changes)
    mean_ret = _mean(changes)
    sharpe = (mean_ret / vol) if vol else 0.0

    sig_adj = _mean(payload.signal[: len(changes)]) if changes else 0.0
    score = float(100.0 * (0.5 * mean_ret - 0.3 * vol + 0.2 * sig_adj))

    base = payload.portfolio_value or 1.0
    curve = [base]
    for c in changes:
        curve.append(curve[-1] * (1.0 + c))
    mdd = _max_drawdown(curve)

    trades_executed = sum(1 for s in payload.signal if s != 0)
    stats: SignalStats = {
        "n": len(changes),
        "sharpe_ratio": float(sharpe),
        "max_drawdown": float(mdd),
        "mean_return": float(mean_ret),
        "volatility": float(vol),
        "trades_executed": int(trades_executed),
    }
    result: SignalResponse = {
        "score": float(score),
        "risk": float(abs(sig_adj)),
        "volatility": float(vol),
        "sharpe_ratio": float(sharpe),
        "max_drawdown": float(mdd),
        "details": stats,
    }
    return result
