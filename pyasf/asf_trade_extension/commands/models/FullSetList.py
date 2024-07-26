import re

from pydantic import BaseModel, model_validator


class Game(BaseModel):
    app_id: int
    cards: int
    set_cards: int
    sets: int


class FullSetList(BaseModel):
    games: list[Game]

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: any) -> dict[str, any]:
        games = []
        lines = data.splitlines()[2:]
        for line in lines:
            digits = re.findall(r"\d+", line)
            game = Game(app_id=digits[0], cards=digits[1], set_cards=digits[2], sets=digits[3])
            games.append(game)
        return {"games": games}
