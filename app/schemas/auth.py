from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserSignup(UserBase):
    password: str = Field(min_length=6, max_length=100)


class UserLogin(UserBase):
    password: str = Field(min_length=6, max_length=100)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class AccessTokenResponse(BaseModel):  # optional
    access_token: str
    token_type: str = "bearer"