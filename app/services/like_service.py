from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import insert, delete

from app.models import Post
from app.models.like import likes  


def toggle_like(db: Session, user, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_like = db.execute(
        likes.select().where(
            (likes.c.user_id == user.id) &
            (likes.c.post_id == post_id)
        )
    ).first()

    if existing_like:
        db.execute(
            delete(likes).where(
                (likes.c.user_id == user.id) &
                (likes.c.post_id == post_id)
            )
        )
        db.commit()

        return {
            "post_id": post_id,
            "liked": False,
            "message": "Post unliked"
        }

    db.execute(
        insert(likes).values(
            user_id=user.id,
            post_id=post_id
        )
    )
    db.commit()

    return {
        "post_id": post_id,
        "liked": True,
        "message": "Post liked"
    }