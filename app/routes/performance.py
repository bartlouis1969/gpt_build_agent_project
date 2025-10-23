from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
import json
import os
from app.main import verify_token

router = APIRouter()
PERFORMANCE_FILE = "performance.json"


class TradeEntry(BaseModel):
    timestamp: datetime | None = None
    pnl: float
    risk: float
    drawdown: float
    notes: str | None = None


class PerformanceKPIs(BaseModel):
    total_trades: int
    total_pnl: float
    avg_pnl: float
    avg_risk: float
    max_drawdown: float
    trades: list[TradeEntry]


def save_trade(entry: TradeEntry):
    entry_dict = entry.dict()
    entry_dict["timestamp"] = (entry.timestamp or datetime.utcnow()).isoformat()
    if not os.path.exists(PERFORMANCE_FILE):
        with open(PERFORMANCE_FILE, "w") as f:
            json.dump([], f)
    with open(PERFORMANCE_FILE, "r+") as f:
        data = json.load(f)
        data.append(entry_dict)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()


@router.post("/analytics/performance", dependencies=[Depends(verify_token)])
def add_trade(entry: TradeEntry):
    save_trade(entry)
    return {"status": "saved", "entry": entry}


@router.get(
    "/analytics/performance",
    response_model=PerformanceKPIs,
    dependencies=[Depends(verify_token)],
)
def get_performance():
    if not os.path.exists(PERFORMANCE_FILE):
        trades = []
    else:
        with open(PERFORMANCE_FILE, "r") as f:
            trades = json.load(f)
    total_trades = len(trades)
    total_pnl = sum(t["pnl"] for t in trades) if trades else 0.0
    avg_pnl = total_pnl / total_trades if total_trades else 0.0
    avg_risk = sum(t["risk"] for t in trades) / total_trades if total_trades else 0.0
    max_drawdown = min((t["drawdown"] for t in trades), default=0.0)
    trade_objs = [TradeEntry(**t) for t in trades]
    return PerformanceKPIs(
        total_trades=total_trades,
        total_pnl=total_pnl,
        avg_pnl=avg_pnl,
        avg_risk=avg_risk,
        max_drawdown=max_drawdown,
        trades=trade_objs,
    )
