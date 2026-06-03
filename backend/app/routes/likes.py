from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.dependencies.auth import get_current_user
from app.schemas.like import LikeResponse
from app.services import like_service

router = APIRouter(prefix="/likes", tags=["Likes"])


@router.post("/{post_id}", response_model=LikeResponse)
def toggle_like(
    post_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return like_service.toggle_like(db, current_user, post_id)