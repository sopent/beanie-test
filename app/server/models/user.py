from beanie import Document
from pydantic import BaseModel
from typing import Optional
import hashlib
import uuid

class User(Document):
    username: str
    password: str
    role: str
    permissions_level: int
    access_token: Optional[uuid.UUID]
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest() # @todo add salt

    def make_access_token(self):
        return uuid.uuid4()
        
    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "username": "test",
                "password": "123456",
                "role": "user",
                "permissions_level": 1,
            }
        }
