from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.core.security import hash_password


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):

    # check if email already exists (older version)
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    print("Password:", user.password)
    print("Length:", len(user.password))
    # hash password
    hashed_pwd = hash_password(user.password)

    # create user object
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd,
        role="developer"  # default role
    )

    # save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user