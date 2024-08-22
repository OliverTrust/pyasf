import re

from pyasf import API, Response
from .models.balance import Balance
from .models.licenses import License, Licenses


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def balance(self) -> Balance:
        res = self._api.command(f"Balance {self.login}")
        return Response[Balance](**res.json()).result

    def level(self) -> int:
        res = self._api.command(f"Level {self.login}")
        result = Response[str](**res.json()).result
        return re.findall(r"\d+", result.split()[-1])[0]

    def loot(
        self, app_id: int, symbol: str | None = None, context_id: int | None = None
    ) -> bool:
        command = "Loot"
        if symbol:
            command += symbol
        command += f" {self.login} {app_id}"
        if context_id:
            command += f" {context_id}"
        res = self._api.command(command)
        result = Response[str](**res.json()).result
        if "error" in result:
            return False
        return True

    def play(self, game: int | str) -> bool:
        res = self._api.command(f"Play {self.login} {game}")
        result = Response[str](**res.json()).result
        if "Done" in result:
            return True
        return False

    def points(self) -> int:
        res = self._api.command(f"Points {self.login}")
        result = Response[str](**res.json()).result
        return re.findall(r"\d+", result.split()[-1])[0]

    def resume(self) -> bool:
        res = self._api.command(f"Resume {self.login}")
        result = Response[str](**res.json()).result
        if "resumed" in result:
            return True
        return False

    def privacy(
        self,
        profile: int = 3,
        owned_games: int = 3,
        play_time: int = 3,
        friends_list: int = 3,
        inventory: int = 3,
        inventory_gifts: int = 3,
        comments: int = 3,
    ) -> bool:
        res = self._api.command(
            f"Privacy {self.login} {profile}, {owned_games}, {play_time}, {friends_list}, {inventory}, {inventory_gifts}, {comments}"
        )
        result = Response[str](**res.json()).result
        if "Success" in result:
            return True
        return False

    def two_fa_ok(self) -> bool:
        res = self._api.command(f"2faok {self.login}")
        result = Response[str](**res.json()).result
        if "Successfully" in result:
            return True
        return False

    def licenses(self) -> list[License]:
        res = self._api.command(f"Licenses {self.login}")
        return Response[Licenses](**res.json()).result.licenses

    def owns(self, game: str) -> int | None:
        """Return app id"""
        res = self._api.command(f"owns {self.login} {game}")
        result = Response[str](**res.json()).result
        match = re.search(r"app/(\d+)", result)
        return match.group(1) if match else None
