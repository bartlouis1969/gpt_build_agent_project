from pydantic import BaseModel, Field
from typing import List, Optional


class SignalCheckRequest(BaseModel):
    signal: List[int] = Field(..., description="1=buy, 0=hold, -1=sell")
    prices: List[float]
    risk_level: Optional[str] = Field(None, description="low | medium | high")
    portfolio_value: Optional[float] = Field(None, description="Voor sizing/simulatie")


class SignalCheckDetails(BaseModel):
    trades_executed: int
    sharpe_ratio: float
    max_drawdown: float


class SignalCheckResponse(BaseModel):
    score: float
    risk: float
    volatility: float
    details: SignalCheckDetails
