from functools import lru_cache

from fastapi import Depends, FastAPI, HTTPException

import config

import motor.motor_asyncio
from beanie import init_beanie
from app.server.models.user import User
from app.server.models.user_account import UserAccount

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()

@app.on_event("startup")
async def start_db():
    settings = get_settings()
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
    await init_beanie(database=getattr(client, settings.db_name), document_models=[User, UserAccount])

@app.get("/")
async def index(settings: config.Settings = Depends(get_settings)):
    return { "App": settings.app_name }

@app.post("/user/", response_description="User added to database")
async def add_user(user: User) -> dict:
    user.access_token = user.make_access_token()
    user.password = user.hash_password(user.password)
    await user.create()
    return {"message": "User %s added successfully" % user.id }

@app.post("/user/account", response_description="User account added to database")
async def add_user_account(user_account: UserAccount) -> dict:
    user = await User.find_one(User.id == user_account.user_id)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="The user does not exists in the system.",
        )
    check_user_account = await UserAccount.find_one(UserAccount.user_id == user_account.user_id)
    if check_user_account is not None:
        raise HTTPException(
            status_code=400,
            detail="The user account already exists in the system and should be updated.",
        )
    await user_account.create()
    return {"message": "User account added successfully"}
