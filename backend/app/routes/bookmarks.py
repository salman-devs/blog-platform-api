from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models import User
from app.services import bookmark_service

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])



@router.post("/{post_id}")
def add_bookmark(
    post_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return bookmark_service.add_bookmark(db, current_user, post_id)



@router.delete("/{post_id}")
def remove_bookmark(
    post_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return bookmark_service.remove_bookmark(db, current_user, post_id)



@router.get("/")
def get_bookmarks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return bookmark_service.get_user_bookmarks(db, current_user)