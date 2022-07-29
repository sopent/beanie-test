from beanie import Document
from iso4217 import Currency
from app.server.lib.object_id import PydanticObjectId


class UserAccount(Document):
    user_id: PydanticObjectId
    currency: Currency
    amount_incoming_payments: float
    count_incoming_payments: int

    class Settings:
        name = "userAccounts"

    class Config:
        schema_extra = {
            "example": {
                "user_id": "62e1a4ef2ca258849b875831",
                "currency": "RUB",
                "amount_incoming_payments": 35.4,
                "count_incoming_payments": 1,
            }
        }
