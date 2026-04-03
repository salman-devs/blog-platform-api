from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.schemas.user import UserResponse


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1, max_length=5000)


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    content: Optional[str] = Field(default=None, min_length=1, max_length=5000)


class PostResponse(PostBase):
    id: int
    owner_id: int
    created_at: datetime

    owner: UserResponse  

    class Config:
        from_attributes = True