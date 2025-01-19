import os
from fastapi import FastAPI
from dotenv import load_dotenv
from routes.chatbot import chatbot_router
from routes.webhooks import webhooks_router
from routes.users import users_router

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="VISDAK Chatbot API", version="1.0")

# Configure database settings
DATABASE_URL = (
    f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@"
    f"{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DATABASE')}"
)

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
