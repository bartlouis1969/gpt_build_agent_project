"""
app/routes/volatility.py

FastAPI endpoint voor volatiliteitsanalyse.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.analytics.volatility import calculate_volatility

router = APIRouter()


class VolatilityRequest(BaseModel):
    prices: list[float]
    window: int = 20


class VolatilityResponse(BaseModel):
    volatilities: list[float]


@router.post("/api/volatility/analyze", response_model=VolatilityResponse)
def analyze_volatility(request: VolatilityRequest):
    try:
        vol = calculate_volatility(request.prices, request.window)
        return VolatilityResponse(volatilities=vol)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
