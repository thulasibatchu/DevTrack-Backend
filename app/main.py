from fastapi import FastAPI

app = FastAPI(title="DevTrack API")


@app.get("/")
def root():
    return {"message": "DevTrack backend running"}
