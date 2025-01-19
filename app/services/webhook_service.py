from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

async def handle_webhook_event(payload: dict):
    """
    Process incoming webhook event.
    """
    try:
        event_type = payload.get("event_type")
        if event_type == "message":
            return {"status": "Message received", "message": payload.get("message")}
        elif event_type == "status_update":
            return {"status": "Status updated", "details": payload.get("status")}
        else:
            return {"status": "Unknown event type", "payload": payload}
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        raise HTTPException(status_code=400, detail="Failed to process webhook")
