from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import post, User

router = APIRouter(prefix="/likes", tags=["likes"])

@router.post("/")
def toggle_like(post_id: int, db: Session = Depends(get_db)):
    user_id = 1
    post = db.query(post).filter(post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    
    user = db.query(User).filter(User.id == user_id).first()

    if post in user.liked_posts:
        user.liked_posts.romove(post)
        db.commit()
        return {"message": "post unliked"}
    
    else:
        user.liked_posts.append(post)
        db.commit()
        return {"message": "post liked"}
    