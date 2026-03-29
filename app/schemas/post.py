from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1, max_length=5000)


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostResponse(PostBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True