from enum import Enum

from pydantic import BaseModel, model_validator


class Token(Enum):
    RUB = "RUB"


class Balance(BaseModel):
    amount: float
    token: Token

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: any) -> dict[str, any]:
        lines = data.split(":")
        balance = lines[1].split()
        return {"amount": float(balance[0].replace(",", ".")), "token": Token(balance[-1])}
