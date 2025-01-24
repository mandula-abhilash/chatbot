import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase

# Load environment variables from .env file
load_dotenv()

# Read database credentials from environment variables
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DATABASE = os.getenv("PG_DATABASE")

# Build the PostgreSQL connection string
DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Initialize the database connection using LangChain
db = SQLDatabase.from_uri(DATABASE_URL)

def init_db():
    """Function to initialize and test the database connection."""
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")  # Simple test query
            print("Database connected successfully!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
