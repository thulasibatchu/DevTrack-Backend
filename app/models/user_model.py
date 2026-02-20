from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="developer")
    created_at = Column(DateTime, default=datetime.utcnow)