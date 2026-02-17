from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User   

app = FastAPI(title="DevTrack API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "DevTrack Backend Running"}
