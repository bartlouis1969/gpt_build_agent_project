from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class PlayerSettingsRequest(BaseModel):
    player_id: str
    account_type: str  # demo/live/funded
    copy_signals: bool
    risk_profile: str | None = "default"


@router.post("/player/settings")
def update_settings(data: PlayerSettingsRequest):
    # Dummy: sla settings op, toggle copy signals
    # In productie: update DB
    return {
        "player_id": data.player_id,
        "account_type": data.account_type,
        "copy_signals": data.copy_signals,
        "risk_profile": data.risk_profile,
        "status": "updated",
    }
