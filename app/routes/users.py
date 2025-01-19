from fastapi import APIRouter
from app.services.user_service import get_users, create_user

users_router = APIRouter()

@users_router.get("/")
async def list_users():
    users = await get_users()
    return {"users": users}

@users_router.post("/")
async def add_user(user: dict):
    new_user = await create_user(user["name"], user["email"])
    return {"message": "User created successfully", "user": new_user}
