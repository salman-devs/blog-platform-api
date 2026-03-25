from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Post
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(
        title=post.title,
        content=post.content,
        owner_id=1 
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/", response_model=list[PostResponse])
def get_posts(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * limit

    posts = db.query(Post).offset(offset).limit(limit).all()

    return posts