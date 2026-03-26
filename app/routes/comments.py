from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Comment
from app.schemas.comment import CommentCreate, CommentResponse

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    new_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        user_id=1  
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment