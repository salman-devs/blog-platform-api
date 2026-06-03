from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User
from app.schemas.comment import CommentCreate, CommentResponse
from app.dependencies.auth import get_current_user
from app.services import comment_service

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/{post_id}", response_model=CommentResponse)
def create_comment(
    post_id: int = Path(..., gt=0),
    comment: CommentCreate = ...,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return comment_service.create_comment(db, current_user.id, comment)


@router.get("/post/{post_id}", response_model=List[CommentResponse])
def get_comments_by_post(
    post_id: int = Path(..., gt=0),
    limit: int = Query(10, ge=1, le=50),
    skip: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    return comment_service.get_comments_by_post(db, post_id, skip, limit)




@router.delete("/{comment_id}")
def delete_comment(
    comment_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return comment_service.delete_comment(db, comment_id, current_user.id)