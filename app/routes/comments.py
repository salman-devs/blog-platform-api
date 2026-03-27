from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Comment,User
from app.schemas.comment import CommentCreate, CommentResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/", response_model=CommentResponse)
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)

):
    new_comment = Comment(
        content=comment.content,
        post_id=comment.post_id,
        user_id=current_user.id  
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment

@router.get("/post/{post_id}", response_model=list[CommentResponse])
def get_comments_by_post(post_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()

    return comments

@router.delete("/{comment_id}")
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db.delete(comment)
    db.commit()

    return {"message": "Comment delete successfully"}
