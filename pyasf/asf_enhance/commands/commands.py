from pyasf import API, validate


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def cartreset(self) -> bool:
        res = self._api.command(f"CARTRESET {self.login}")
        result = validate(res, str).result
        if "Success" in result:
            return True
        return False

    def addcart(self, name: str) -> bool:
        # s/1234, b/1234
        res = self._api.command(f"ADDCART {self.login} {name}")
        result = validate(res, str).result
        if "√" in result:
            return True
        return False

    def purchase(self) -> bool:
        res = self._api.command(f"PURCHASE {self.login}")
        result = validate(res, str).result
        if "done" in result:
            return True
        return False

    def CraftBadge(self) -> bool:
        res = self._api.command(f"CRAFTBADGE {self.login}")
        result = validate(res, str).result
        if "successful" in result:
            return True
        return False
