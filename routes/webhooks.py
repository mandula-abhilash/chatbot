from fastapi import APIRouter, Request

webhooks_router = APIRouter()

@webhooks_router.post("/")
async def handle_webhook(request: Request):
    """
    Endpoint to handle webhooks from Meta or WhatsApp.
    """
    data = await request.json()
    # Add logic to process webhook payload
    return {"message": "Webhook received", "data": data}
