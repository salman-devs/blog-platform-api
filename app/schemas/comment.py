from pydantic import BaseModel, Field
from datetime import datetime
from app.schemas.user import UserResponse


class CommentBase(BaseModel):
    content: str = Field(min_length=1, max_length=1000)


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class CommentResponse(CommentBase):
    id: int
    user_id: int
    post_id: int
    created_at: datetime

    user: UserResponse  

    class Config:
        from_attributes = True