from sqlmodel import SQLModel, Field
from typing import Optional, List
from pydantic import EmailStr
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(primary_key=True)
    fullname: Optional[str]
    username: Optional[str]
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    profile_url: Optional[str] = Field(default=None)

