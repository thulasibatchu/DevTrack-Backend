from fastapi import FastAPI
from app.models import user_model
from app.core.database import Base, engine

app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "DevTrack backend running"}
