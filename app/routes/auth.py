from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.schemas.auth import UserSignup, UserLogin, TokenResponse, AccessTokenResponse
from app.schemas.user import UserResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


class RefreshRequest(BaseModel):
    refresh_token: str


@router.post("/signup", response_model=UserResponse)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    return auth_service.signup_user(user, db)


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return auth_service.login_user(user, db)


@router.post("/refresh", response_model=AccessTokenResponse)
def refresh_token(data: RefreshRequest):
    return auth_service.refresh_access_token(data.refresh_token)