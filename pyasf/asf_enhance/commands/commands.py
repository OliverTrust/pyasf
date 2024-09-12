from pyasf import API, Response
from pyasf.asf_enhance.models.cookies import Cookies


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def cart_reset(self) -> bool:
        res = self._api.command(f"CartReset {self.login}")
        result = Response[str](**res.json()).result
        if "Success" in result:
            return True
        return False

    def add_cart(self, name: str) -> bool:
        # s/1234, b/1234
        res = self._api.command(f"AddCart {self.login} {name}")
        result = Response[str](**res.json()).result
        if "√" in result:
            return True
        return False

    def purchase(self) -> bool:
        res = self._api.command(f"Purchase {self.login}")
        result = Response[str](**res.json()).result
        if "done" in result:
            return True
        return False

    def craft_badge(self) -> bool:
        res = self._api.command(f"CraftBadge {self.login}")
        result = Response[str](**res.json()).result
        if "successful" in result:
            return True
        return False

    def add_friend(self, text: str) -> bool:
        res = self._api.command(f"AddFriend {self.login} {text}")
        result = Response[str](**res.json()).result
        if "successful" in result:
            return True
        return False

    def cookies(self) -> Cookies:
        res = self._api.command(f"Cookies {self.login}")
        return Response[Cookies](**res.json()).result
