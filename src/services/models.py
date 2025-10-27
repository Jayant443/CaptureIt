from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Image(SQLModel, table=True):
    __tablename__ = "images"

    id: Optional[int] = Field(default=None, primary_key=True)
    image_url: str
    user_id: int = Field(foreign_key="users.id")
    title: Optional[str] = None
    likes: int = Field(default=0)
    views: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Like(SQLModel, table=True):
    __tablename__ = "likes"

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    image_id: int = Field(foreign_key="images.id", primary_key=True)


class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    image_id: int = Field(foreign_key="images.id")
    parent_id: Optional[int] = Field(default=None, foreign_key="comments.id")
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
