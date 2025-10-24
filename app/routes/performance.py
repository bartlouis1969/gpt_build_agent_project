from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.auth_utils import verify_token

router = APIRouter()


class TradeIn(BaseModel):
    pnl: float
    risk: float
    drawdown: float
    notes: str


_TRADES: list[TradeIn] = []


@router.post("/performance")
def add_trade(trade: TradeIn, _: str = Depends(verify_token)) -> dict:
    _TRADES.append(trade)
    return {"status": "saved", **trade.model_dump()}


@router.get("/performance")
def list_trades(_: str = Depends(verify_token)) -> dict:
    items = [t.model_dump() for t in _TRADES]
    total_pnl = sum(t.pnl for t in _TRADES) if _TRADES else 0.0
    avg_pnl = (total_pnl / len(_TRADES)) if _TRADES else 0.0
    avg_risk = (sum(t.risk for t in _TRADES) / len(_TRADES)) if _TRADES else 0.0
    max_drawdown = min((t.drawdown for t in _TRADES), default=0.0)  # kan negatief zijn

    return {
        "total_trades": len(items),
        "total_pnl": float(total_pnl),
        "avg_pnl": float(avg_pnl),
        "avg_risk": float(avg_risk),
        "max_drawdown": float(max_drawdown),
        "trades": items,
    }
