from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Post


def create_post(db: Session, user_id: int, post_data):
    new_post = Post(
        title=post_data.title,
        content=post_data.content,
        owner_id=user_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_posts(db: Session, page: int, limit: int, search: str):
    skip = (page - 1) * limit

    query = db.query(Post)

    if search:
        query = query.filter(
            Post.title.ilike(f"%{search}%") |
            Post.content.ilike(f"%{search}%")
        )

    total = query.count()

    posts = (
        query
        .order_by(Post.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": posts
    }


def get_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


def update_post(db: Session, post_id: int, user_id: int, updated_post):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    if updated_post.title is not None:
        post.title = updated_post.title

    if updated_post.content is not None:
        post.content = updated_post.content

    db.commit()
    db.refresh(post)

    return post


def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(post)
    db.commit()

    return {"message": "Post deleted successfully"}