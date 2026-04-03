from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Comment, Post


def create_comment(db: Session, user_id: int, comment_data):
    post = db.query(Post).filter(Post.id == comment_data.post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    new_comment = Comment(
        content=comment_data.content,
        post_id=comment_data.post_id,
        user_id=user_id
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


def get_comments_by_post(db: Session, post_id: int, skip: int, limit: int):
    return (
        db.query(Comment)
        .filter(Comment.post_id == post_id)
        .order_by(Comment.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_comment(db: Session, comment_id: int, user_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(comment)
    db.commit()

    return {"message": "Comment deleted successfully"}