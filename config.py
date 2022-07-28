from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Test API"
    mongodb_url: str
    db_name: str

    class Config:
        env_file = ".env"
