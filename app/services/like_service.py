from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Post, Like


def toggle_like(db: Session, user, post_id: int):

    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_like = db.query(Like).filter(
        Like.user_id == user.id,
        Like.post_id == post_id
    ).first()

    if existing_like:
        db.delete(existing_like)
        db.commit()
        return {
            "post_id": post_id,
            "liked": False,
            "message": "Post unliked"
        }

    new_like = Like(
        user_id=user.id,
        post_id=post_id
    )

    db.add(new_like)
    db.commit()

    return {
        "post_id": post_id,
        "liked": True,
        "message": "Post liked"
    }