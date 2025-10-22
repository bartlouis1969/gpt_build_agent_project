from fastapi import FastAPI
from app.routes.volatility import router as volatility_router
from app.routes.ai_generator import router as ai_router
from app.routes.memory import router as memory_router
from app.routes.signal_check import router as signal_check_router

app = FastAPI()
app.include_router(volatility_router)
app.include_router(ai_router)
app.include_router(memory_router)
app.include_router(signal_check_router)


@app.get("/health")
def health():
    return {"status": "ok"}
