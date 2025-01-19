from fastapi import APIRouter
from app.services.chatbot_service import process_chat

chatbot_router = APIRouter()

@chatbot_router.post("/")
async def process_query(query: dict):
    user_query = query.get("query", "")
    response = await process_chat(user_query)
    return {"response": response}
