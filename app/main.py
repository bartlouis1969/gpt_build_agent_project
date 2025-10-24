from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth_utils import create_access_token, verify_token
from app.routes.ai_generator import router as ai_router
from app.routes.download import router as download_router
from app.routes.feedback import router as feedback_router
from app.routes.memory import router as memory_router
from app.routes.performance import router as performance_router
from app.routes.signal_check import router as signal_router

app = FastAPI(title="EA Landing API", version="1.0.0")


# --- Auth endpoint (dummy login) -------------------------------------------------
@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # Dummy login: admin/admin
    if form_data.username == "admin" and form_data.password == "admin":
        token = create_access_token(form_data.username)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )


# --- Routers ---------------------------------------------------------------------
# Publiek

app.include_router(ai_router, prefix="/ai", tags=["ai"])
app.include_router(signal_router, prefix="/analytics", tags=["analytics"])
app.include_router(download_router, tags=["download"])

# Protected (Bearer)
protected = [Depends(verify_token)]
app.include_router(
    feedback_router,
    prefix="/ai",
    tags=["feedback"],
    dependencies=protected,
)
app.include_router(
    performance_router,
    prefix="/analytics",
    tags=["performance"],
    dependencies=protected,
)

# Memory is public (tests expect 200/404 without auth)
app.include_router(memory_router, prefix="/ai", tags=["memory"])


# --- Health ----------------------------------------------------------------------
@app.get("/healthz")
def health():
    return {"status": "ok"}
