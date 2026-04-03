from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

# Association table for many-to-many relationship between users and posts
likes = Table(
    "likes",
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    ),
    Column(
        "post_id",
        Integer,
        ForeignKey("posts.id", ondelete="CASCADE"),
        primary_key=True
    )
)