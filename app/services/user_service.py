from app.models.database import AsyncSessionLocal
from app.models.user_model import User
from sqlalchemy import select

async def get_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        return result.scalars().all()
    
async def create_user(name: str, email: str):
    async with AsyncSessionLocal() as session:
        new_user = User(name=name, email=email)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user