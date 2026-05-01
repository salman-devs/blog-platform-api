from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS


def create_access_token(data: dict):
    if "sub" not in data:
        raise ValueError("Token must include 'sub'")

    to_encode = data.copy()
    to_encode["type"] = "access"

    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({
        "exp": expire,
        "iat": now
    })

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    if "sub" not in data:
        raise ValueError("Token must include 'sub'")

    to_encode = data.copy()
    to_encode["type"] = "refresh"

    now = datetime.now(timezone.utc)
    expire = now + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    to_encode.update({
        "exp": expire,
        "iat": now
    })

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)