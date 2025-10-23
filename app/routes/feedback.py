from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
import json
import os
from app.main import verify_token

router = APIRouter()
LESSONS_FILE = "lessons.json"


class FeedbackEntry(BaseModel):
    user: str
    feedback: str
    timestamp: datetime | None = None


class FeedbackResponse(BaseModel):
    status: str
    entry: FeedbackEntry


def save_feedback(entry: FeedbackEntry):
    entry_dict = entry.dict()
    if entry.timestamp is not None:
        entry_dict["timestamp"] = entry.timestamp.isoformat()
    else:
        entry_dict["timestamp"] = datetime.utcnow().isoformat()
    if not os.path.exists(LESSONS_FILE):
        with open(LESSONS_FILE, "w") as f:
            json.dump([], f)
    with open(LESSONS_FILE, "r+") as f:
        data = json.load(f)
        data.append(entry_dict)
        f.seek(0)
        json.dump(data, f, indent=2)
    f.truncate()


@router.post(
    "/ai/feedback",
    response_model=FeedbackResponse,
    dependencies=[Depends(verify_token)],
)
def add_feedback(entry: FeedbackEntry):
    entry.timestamp = datetime.utcnow()
    save_feedback(entry)
    return FeedbackResponse(status="saved", entry=entry)


@router.get("/ai/feedback", dependencies=[Depends(verify_token)])
def get_feedback():
    if not os.path.exists(LESSONS_FILE):
        return []
    with open(LESSONS_FILE, "r") as f:
        return json.load(f)
