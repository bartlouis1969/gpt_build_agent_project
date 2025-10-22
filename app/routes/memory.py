from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime


router = APIRouter()

# In-memory memory store
memory_store = {}


class MemoryEntry(BaseModel):
    key: str
    value: str


class MemoryResponse(BaseModel):
    key: str
    value: str
    timestamp: datetime


@router.post("/ai/memory", response_model=MemoryResponse)
def set_memory(entry: MemoryEntry):
    now = datetime.utcnow()
    memory_store[entry.key] = {"value": entry.value, "timestamp": now}
    return {"key": entry.key, "value": entry.value, "timestamp": now}


@router.get("/ai/memory/{key}", response_model=MemoryResponse)
def get_memory(key: str):
    if key not in memory_store:
        raise HTTPException(status_code=404, detail="Key not found")
    entry = memory_store[key]
    return {"key": key, "value": entry["value"], "timestamp": entry["timestamp"]}


@router.get("/ai/memory")
def get_all_memory():
    return [
        {"key": k, "value": v["value"], "timestamp": v["timestamp"]}
        for k, v in memory_store.items()
    ]
