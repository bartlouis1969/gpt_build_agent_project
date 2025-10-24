from pydantic import BaseModel, Field


class SignalCheckRequest(BaseModel):
    signal: list[int] = Field(..., description="1=buy, 0=hold, -1=sell")
    prices: list[float]
    risk_level: str | None = Field(None, description="low | medium | high")
    portfolio_value: float | None = Field(None, description="Voor sizing/simulatie")


class SignalCheckDetails(BaseModel):
    trades_executed: int
    sharpe_ratio: float
    max_drawdown: float


class SignalCheckResponse(BaseModel):
    score: float
    risk: float
    volatility: float
    details: SignalCheckDetails
