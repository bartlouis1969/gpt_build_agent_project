from fastapi import APIRouter
from core.analytics.signal_check_models import (
    SignalCheckRequest,
    SignalCheckResponse,
    SignalCheckDetails,
)

router = APIRouter()


@router.post("/analytics/signal-check", response_model=SignalCheckResponse)
def signal_check(request: SignalCheckRequest) -> SignalCheckResponse:
    # Dummy logic, replace with real analytics/backtest
    trades_executed = sum(1 for s in request.signal if s != 0)
    sharpe_ratio = 1.12  # Placeholder
    max_drawdown = 0.06  # Placeholder
    score = 0.82  # Placeholder
    risk = 0.45  # Placeholder
    volatility = 0.12  # Placeholder
    details = SignalCheckDetails(
        trades_executed=trades_executed,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown,
    )
    return SignalCheckResponse(
        score=score, risk=risk, volatility=volatility, details=details
    )
