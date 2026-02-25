from pydantic import BaseModel, EmailStr,Field
from datetime import datetime


# Schema used when creating a user (request body)


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


# Schema used when returning user data (response)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime

    class Config:
        from_attributes = True