from __future__ import annotations

from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def create_access_token(username: str, expires_delta: timedelta | None = None) -> str:
    # expires_delta wordt genegeerd in deze dummy-implementatie
    return f"user:{username}"


def verify_token(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
    if not token or not token.startswith("user:"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username = token.split(":", 1)[1] or "anonymous"
    return {"sub": username}
