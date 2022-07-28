from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Test API"

    class Config:
        env_file = ".env"
