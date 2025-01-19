from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatbotQuery(Base):
    __tablename__ = "chatbot_queries"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
