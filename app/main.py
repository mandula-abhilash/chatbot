import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.utils.logger import logger
from app.routes.chatbot import chatbot_router
from app.routes.webhooks import webhooks_router
from app.routes.users import users_router
from app.models.database import init_db  

# Load environment variables
load_dotenv()

print("PG_HOST:", os.getenv("PG_HOST"))
print("PG_PORT:", os.getenv("PG_PORT"))
print("PG_USER:", os.getenv("PG_USER"))
print("PG_PASSWORD:", os.getenv("PG_PASSWORD"))
print("PG_DATABASE:", os.getenv("PG_DATABASE"))

# Initialize FastAPI app
app = FastAPI(title="VISDAK Chatbot API", version="1.0")

logger.info("VISDAK Chatbot API is starting...")

# Configure database settings
DATABASE_URL = (
    f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@"
    f"{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DATABASE')}"
)

# Initialize database
@app.on_event("startup")
async def startup_event():
    await init_db()  # Ensure the database is initialized

# Register routers
app.include_router(chatbot_router, prefix="/chat", tags=["Chatbot"])
app.include_router(webhooks_router, prefix="/webhook", tags=["Webhooks"])
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
