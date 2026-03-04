from fastapi import FastAPI
from app.models import user_model
from app.core.database import Base, engine
from app.api.user_routes import router as user_router
from app.models import project_model
from app.api import project_routes


app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)




app.include_router(user_router)
app.include_router(project_routes.router)
