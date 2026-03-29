from pydantic import BaseModel, Field

class LikeRequest(BaseModel):
    post_id: int = Field(gt=0)
    