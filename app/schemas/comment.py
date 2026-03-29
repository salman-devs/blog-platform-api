from pydantic import BaseModel, Field
from datetime import datetime


class CommentCreate(BaseModel):
    content: str = Field(min_length=1, max_length=1000)


class CommentResponse(BaseModel):
    id: int
    content: str
    user_id: int
    post_id: int
    created_at: datetime

    class Config:
        from_attributes = True