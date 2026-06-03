from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base


likes = Table(
    "likes",
    Base.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True, index=True
    ),
    Column(
        "post_id",
        Integer,
        ForeignKey("posts.id", ondelete="CASCADE"),
        primary_key=True
    )
)
