from fastapi import APIRouter, Request
from app.services.webhook_service import handle_webhook_event

webhooks_router = APIRouter()

@webhooks_router.post("/")
async def receive_webhook(request: Request):
    payload = await request.json()
    response = await handle_webhook_event(payload)
    return {"message": "Webhook processed", "details": response}
