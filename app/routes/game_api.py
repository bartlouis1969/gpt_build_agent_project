from fastapi import APIRouter
from pydantic import BaseModel

from app.connectors.mt5_connector import MT5Connector

router = APIRouter()


# --- Models ---
class LoginRequest(BaseModel):
    email: str | None = None
    player_name: str | None = None


class CreditsUpdateRequest(BaseModel):
    player_id: str
    amount: int
    action: str  # 'add', 'spend', 'reward'


class AIChatRequest(BaseModel):
    player_id: str
    message: str


class FeedbackRequest(BaseModel):
    player_id: str
    challenge_id: str
    result: str
    choices: dict | None = None
    ai_feedback: str | None = None


class TradingSetupRequest(BaseModel):
    player_id: str
    symbol: str
    risk: float
    lot_size: float
    stop_loss: int
    account_type: str  # demo or real


class MT5ConnectRequest(BaseModel):
    player_id: str
    account_type: str  # demo or real


# --- Endpoints ---
@router.post("/login")
def login(data: LoginRequest):
    if data.email:
        return {"token": "demo-token", "player_id": data.email}
    if data.player_name:
        return {"token": None, "player_id": data.player_name}
    return {"token": None, "player_id": "guest"}


@router.get("/credits")
def get_credits(player_id: str):
    return {"player_id": player_id, "credits": 100}


@router.post("/credits/update")
def update_credits(data: CreditsUpdateRequest):
    return {
        "player_id": data.player_id,
        "new_credits": 100 + data.amount,
        "action": data.action,
    }


@router.post("/ai/chat")
def ai_chat(data: AIChatRequest):
    return {"response": f"AI says: You said '{data.message}'"}


@router.post("/feedback")
def log_feedback(data: FeedbackRequest):
    return {
        "status": "ok",
        "player_id": data.player_id,
        "challenge_id": data.challenge_id,
    }


# --- TradingView/MT5 integratie ---
@router.post("/game/trading-setup")
def trading_setup(data: TradingSetupRequest):
    # Simuleer opslaan van setup en uitvoeren trade via MT5Connector
    mt5 = MT5Connector(account_type=data.account_type)
    mt5.connect()
    trade_result = mt5.place_trade(
        symbol=data.symbol,
        lot_size=data.lot_size,
        stop_loss=data.stop_loss,
        risk=data.risk,
    )
    mt5.disconnect()
    # In productie: sla setup en resultaat op in DB
    return {"status": "ok", "trade_result": trade_result}


@router.post("/game/mt5-connect")
def mt5_connect(data: MT5ConnectRequest):
    mt5 = MT5Connector(account_type=data.account_type)
    connected = mt5.connect()
    return {
        "status": "connected" if connected else "failed",
        "account_type": data.account_type,
    }
