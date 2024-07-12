from pyasf import API, validate
from .models.player_profile import PlayerProfile


class IPC:
    _api_path = "Api/CS2Interface"

    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def start(self) -> None:
        path = f"{self._api_path}/{self.login}/Start"
        self._api.request("GET", path, None)

    def stop(self) -> None:
        path = f"{self._api_path}/{self.login}/Stop"
        self._api.request("GET", path, None)

    def playerprofile(self, id64: int | str) -> PlayerProfile:
        path = f"{self._api_path}/{self.login}/PlayerProfile/{id64}"
        res = self._api.request("GET", path, None)
        return validate(res, PlayerProfile).result
