from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List, Optional

class UserBase(BaseModel):
    fullname: str
    email: EmailStr
    username: Optional[str]
    profile_url: Optional[str] = None
    
class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserSchema(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)