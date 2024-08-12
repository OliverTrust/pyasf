from .models.full_set_list import FullSetList
from pyasf import API, Response


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def full_set_list(
        self, page: int | None = None, line: int | None = None
    ) -> FullSetList:
        command = f"FullSetList {self.login}"
        if page:
            command += f" -page {page}"
        if line:
            command += f" -line {line}"
        res = self._api.command(command)
        return Response[FullSetList](**res.json()).result

    def two_send_card_set(self, app_id: int, sets: int, trade_url: str) -> bool:
        command = f"2SendCardSet {self.login} {app_id} {sets} {trade_url}"
        res = self._api.command(command)
        result = Response[str](**res.json()).result
        if "sent Success" in result:
            return True
        return False
