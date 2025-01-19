from app.models.database import SessionLocal
from app.models.user_model import User

async def get_users():
    async with SessionLocal() as session:
        result = await session.execute("SELECT * FROM users")
        return result.fetchall()
    
async def create_user(name: str, email: str):
    async with SessionLocal() as session:
        new_user = User(name=name, email=email)
        session.add(new_user)
        await session.commit()
        return new_user
