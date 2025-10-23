if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from app.routes.volatility import router as volatility_router
from app.routes.ai_generator import router as ai_router
from app.routes.memory import router as memory_router
from app.routes.signal_check import router as signal_check_router
import importlib.util
import glob
import os

SECRET_KEY = "supersecretkey"  # Zet in .env voor productie
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


app = FastAPI()
app.include_router(volatility_router, dependencies=[Depends(verify_token)])
app.include_router(ai_router, dependencies=[Depends(verify_token)])
app.include_router(memory_router, dependencies=[Depends(verify_token)])
app.include_router(signal_check_router, dependencies=[Depends(verify_token)])

# Dynamisch plugins laden uit plugins/
PLUGINS_DIR = os.path.join(os.path.dirname(__file__), "..", "plugins")
plugin_files = glob.glob(os.path.join(PLUGINS_DIR, "*.py"))
for plugin_path in plugin_files:
    module_name = os.path.splitext(os.path.basename(plugin_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, plugin_path)
    if spec is not None and spec.loader is not None:
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        if hasattr(plugin_module, "router"):
            app.include_router(plugin_module.router)


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Dummy user, vervang door echte user-check
    if form_data.username == "admin" and form_data.password == "admin":
        access_token = create_access_token(
            data={"sub": form_data.username},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")


@app.get("/health")
def health():
    return {"status": "ok"}
