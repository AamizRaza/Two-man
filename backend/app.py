from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import SessionLocal, engine
from . import models

# create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# allow cross-origin requests from any origin (use restrictive list in production)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StreakRequest(BaseModel):
    nickname: str


class StreakResponse(BaseModel):
    nickname: str
    streak: int


@app.post("/streak", response_model=StreakResponse)
def increment_streak(req: StreakRequest):
    db = SessionLocal()
    try:
        user = db.query(models.User).filter(models.User.nickname == req.nickname).first()
        if user:
            user.streak += 1
        else:
            user = models.User(nickname=req.nickname, streak=1)
            db.add(user)
        db.commit()
        db.refresh(user)
        return StreakResponse(nickname=user.nickname, streak=user.streak)
    finally:
        db.close()
