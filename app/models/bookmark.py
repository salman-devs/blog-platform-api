from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.database import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "post_id", name="unique_user_post"),
    )