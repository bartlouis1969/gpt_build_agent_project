from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.auth_utils import verify_token

router = APIRouter()


class FeedbackIn(BaseModel):
    user: str
    feedback: str


_FEEDBACKS: list[FeedbackIn] = []


@router.post("/feedback")
def add_feedback(item: FeedbackIn, _: str = Depends(verify_token)) -> dict:
    _FEEDBACKS.append(item)
    return {"status": "saved", "entry": item.model_dump()}


@router.get("/feedback")
def list_feedback(_: str = Depends(verify_token)) -> list[dict]:
    return [f.model_dump() for f in _FEEDBACKS]
