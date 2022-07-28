from functools import lru_cache

from fastapi import Depends, FastAPI, HTTPException

import config

@lru_cache()
def get_settings():
    return config.Settings()

app = FastAPI()

@app.get("/")
async def index(settings: config.Settings = Depends(get_settings)):
    return { "App": settings.app_name }

