from fastapi import FastAPI
from app.routes.volatility import router as volatility_router
from app.routes.ai_generator import router as ai_router

app = FastAPI()
app.include_router(volatility_router)
app.include_router(ai_router)


@app.get("/health")
def health():
    return {"status": "ok"}
