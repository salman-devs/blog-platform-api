from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Post


def toggle_like(db: Session, user, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post in user.liked_posts:
        user.liked_posts.remove(post)
        db.commit()
        return {
            "post_id": post_id,
            "liked": False
        }

    else:
        user.liked_posts.append(post)
        db.commit()
        return {
            "post_id": post_id,
            "liked": True
        }