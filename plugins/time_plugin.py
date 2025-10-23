from fastapi import APIRouter

router = APIRouter()


@router.get("/plugin/time")
def plugin_time():
    from datetime import datetime

    return {"server_time": datetime.utcnow().isoformat()}
