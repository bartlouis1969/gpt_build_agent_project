from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class MemoryItem(BaseModel):
    key: str
    value: str


_MEMORY: dict[str, dict] = {}  # store with timestamp


@router.post("/memory")
def set_memory(item: MemoryItem) -> dict:
    payload = {
        "key": item.key,
        "value": item.value,
        "timestamp": datetime.now(UTC).isoformat(),
    }
    _MEMORY[item.key] = payload
    return payload


@router.get("/memory")
def get_all_memory() -> list[dict]:
    return list(_MEMORY.values())


@router.get("/memory/{key}")
def get_memory_key(key: str) -> dict:
    if key not in _MEMORY:
        raise HTTPException(status_code=404, detail="Key not found")
    return _MEMORY[key]
