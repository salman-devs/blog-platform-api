from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.like import likes


class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    posts = relationship("Post", back_populates="owner", cascade="all,delete")
    comments = relationship("Comment", back_populates="user", cascade="all, delete")
    liked_posts = relationship("Post", secondary=likes, back_populates="liked_by")
    