from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/download")
def download_placeholder() -> dict[str, str]:
    """
    Placeholder endpoint zodat imports/routers kloppen.
    Je  v0.2 verifier  kun je hier later (opnieuw) inhangen.
    """
    return {"ok": "True", "msg": "Download endpoint online"}
