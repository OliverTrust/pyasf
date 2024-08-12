from pyasf import API, Response
from .models.player_profile import PlayerProfile


class IPC:
    _api_path = "Api/CS2Interface"

    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def start(self) -> bool:
        path = f"{self._api_path}/{self.login}/Start"
        res = self._api.request("GET", path, None)
        if res.status_code == 200:
            return True
        return False

    def stop(self) -> bool:
        path = f"{self._api_path}/{self.login}/Stop"
        res = self._api.request("GET", path, None)
        if res.status_code == 200:
            return True
        return False

    def player_profile(self, id64: int | str) -> PlayerProfile:
        path = f"{self._api_path}/{self.login}/PlayerProfile/{id64}"
        res = self._api.request("GET", path, None)
        return Response[PlayerProfile](**res.json()).result
