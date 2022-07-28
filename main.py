from functools import lru_cache

from fastapi import Depends, FastAPI, HTTPException

import config

import motor.motor_asyncio
from beanie import init_beanie
from app.server.models.user import User

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()

@app.on_event("startup")
async def start_db():
    settings = get_settings()
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
    await init_beanie(database=getattr(client, settings.db_name), document_models=[User])

@app.get("/")
async def index(settings: config.Settings = Depends(get_settings)):
    return { "App": settings.app_name }

@app.post("/user/", response_description="User added to database")
async def add_user(user: User) -> dict:
    await user.create() # test save to database
    return {"message": "ok"}
    
@app.post("/user/account", response_description="User account added to database")
async def add_user_account(user_account) -> dict:
    return {"message": "ok"}
