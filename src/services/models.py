from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class Photo(SQLModel):
    __tablename__ = "photos"

    id: Optional[int] = Field(primary_key=True)
    image_url: str
    user_id: int = Field(foreign_key="users.id")
    title: Optional[str]
    likes: int = Field(default=0)
    views: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)