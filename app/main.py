import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from app.utils.logger import logger
from app.routes.chatbot import chatbot_router
from app.routes.webhooks import webhooks_router
from app.routes.users import users_router
from app.models.database import init_db  
import logging

# Enhanced logging setup
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console handler
        logging.FileHandler('debug.log')  # File handler
    ]
)

# Load environment variables
load_dotenv()

# Add debug prints for environment variables
logger.debug("Environment Variables:")
logger.debug(f"PG_HOST: {os.getenv('PG_HOST')}")
logger.debug(f"PG_PORT: {os.getenv('PG_PORT')}")
logger.debug(f"PG_USER: {os.getenv('PG_USER')}")
logger.debug(f"PG_DATABASE: {os.getenv('PG_DATABASE')}")

# Define lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        logger.info("Starting up database...")
        await init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise
    yield
    # Shutdown
    logger.info("Shutting down...")

# Initialize FastAPI app with debug mode and lifespan
app = FastAPI(
    title="VISDAK Chatbot API",
    version="1.0",
    debug=True,  # Enable debug mode
    lifespan=lifespan
)

logger.info("VISDAK Chatbot API is starting...")

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
    logger.debug("Health check endpoint called")
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload
        log_level="debug"  # Set Uvicorn log level to debug
    )