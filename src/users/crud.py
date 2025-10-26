from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Optional
from sqlmodel import select
from .models import User
from src.auth.hash import hash_password
from .schemas import UserCreate, UserUpdate


class UserCrud:
    async def create_user(self, user: UserCreate, session: AsyncSession):
        user_data = user.model_dump()
        user_data["password"] = hash_password(user_data["password"])
        new_user = User(**user_data)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
    
    async def get_user(self, username: str, session: AsyncSession) -> Optional[User]:
        result = await session.exec(select(User).where(User.username==username))
        return result.first()
    
# some other functions to be added:
# update_user
# delete_user
# and some other functions
