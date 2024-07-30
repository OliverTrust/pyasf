import re

from pyasf import API, validate
from .models.balance import Balance


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def balance(self) -> Balance:
        res = self._api.command(f"Balance {self.login}")
        return validate(res, Balance).result

    def level(self) -> int:
        res = self._api.command(f"Level {self.login}")
        result = validate(res, str).result
        return re.findall(r"\d+", result.split()[-1])[0]

    def loot(self, app_id: int, symbol: str | None = None, context_id: int | None = None) -> bool:
        command = "Loot"
        if symbol:
            command += symbol
        command += f" {self.login} {app_id}"
        if context_id:
            command += f" {context_id}"
        res = self._api.command(command)
        result = validate(res, str).result
        if "error" in result:
            return False
        return True

    def play(self, game: int | str) -> bool:
        res = self._api.command(f"Play {self.login} {game}")
        result = validate(res, str).result
        if "Done" in result:
            return True
        return False

    def points(self) -> int:
        res = self._api.command(f"Points {self.login}")
        result = validate(res, str).result
        return re.findall(r"\d+", result.split()[-1])[0]

    def resume(self) -> bool:
        res = self._api.command(f"Resume {self.login}")
        result = validate(res, str).result
        if "resumed" in result:
            return True
        return False

    def privacy(self, profile: int = 3, owned_games: int = 3, play_time: int = 3, friends_list: int = 3, inventory: int = 3, inventory_gifts: int = 3, comments: int = 3) -> bool:
        res = self._api.command(f"Privacy {self.login} {profile}, {owned_games}, {play_time}, {friends_list}, {inventory}, {inventory_gifts}, {comments}")
        result = validate(res, str).result
        if "Success" in result:
            return True
        return False

    def twofaok(self) -> bool:
        res = self._api.command(f"2faok {self.login}")
        result = validate(res, str).result
        if "Successfully" in result:
            return True
        return False
