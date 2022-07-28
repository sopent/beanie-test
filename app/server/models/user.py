from beanie import Document

class User(Document):
    username: str

    class Settings:
        name = "users"
