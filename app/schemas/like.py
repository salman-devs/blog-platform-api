from pydantic import BaseModel

class LikeRequest(BaseModel):
    post_id: int
    