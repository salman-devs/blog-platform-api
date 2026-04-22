from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models import User
from app.schemas.post import PostCreate, PostResponse, PostUpdate, PostListResponse
from app.services import post_service

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse, status_code=201)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return post_service.create_post(db, current_user.id, post)


@router.get("/", response_model=PostListResponse)
def get_posts(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    search: Optional[str] = Query(None),
    user_id: Optional[int] = Query(None, gt=0),
    db: Session = Depends(get_db)
):
    return post_service.get_posts(db, page, limit, search, user_id)


@router.get("/{post_id}", response_model=PostResponse)
def get_post(
    post_id: int = Path(..., gt=0),
    db: Session = Depends(get_db)
):
    return post_service.get_post_by_id(db, post_id)


@router.put("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int = Path(..., gt=0),
    updated_post : PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return post_service.update_post(db, post_id, current_user.id, updated_post)


@router.delete("/{post_id}")
def delete_post(
    post_id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return post_service.delete_post(db, post_id, current_user.id)