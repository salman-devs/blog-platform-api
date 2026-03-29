from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Post, User
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/likes", tags=["Likes"])


@router.post("/{post_id}")
def toggle_like(
    post_id: int = Path(gt=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    user = current_user

    if post in user.liked_posts:
        user.liked_posts.remove(post)
        db.commit()
        return {"message": "Post unliked successfully"}

    else:
        user.liked_posts.append(post)
        db.commit()
        return {"message": "Post liked successfully"}