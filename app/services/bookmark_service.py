from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Bookmark, Post



def add_bookmark(db: Session, user, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing = db.query(Bookmark).filter(
        Bookmark.user_id == user.id,
        Bookmark.post_id == post_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already bookmarked")

    bookmark = Bookmark(user_id=user.id, post_id=post_id)

    db.add(bookmark)
    db.commit()

    return {"message": "Post bookmarked"}


def remove_bookmark(db: Session, user, post_id: int):
    bookmark = db.query(Bookmark).filter(
        Bookmark.user_id == user.id,
        Bookmark.post_id == post_id
    ).first()

    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    db.delete(bookmark)
    db.commit()

    return {"message": "Bookmark removed"}


def get_user_bookmarks(db: Session, user):
    return (
        db.query(Post)
        .join(Bookmark, Bookmark.post_id == Post.id)
        .filter(Bookmark.user_id == user.id)
        .all()
    )