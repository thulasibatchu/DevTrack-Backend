from fastapi import FastAPI
from app.models import user_model
from app.core.database import Base, engine
from app.api.user_routes import router as user_router

app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)




app.include_router(user_router)