from pydantic import BaseModel, Field


class LikeCreate(BaseModel):
    post_id: int = Field(gt=0)


class LikeResponse(BaseModel):
    post_id: int
    liked: bool