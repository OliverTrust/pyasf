from .models.FullSetList import FullSetList
from pyasf import API, validate


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def FullSetList(self, page: int | None = None, line: int | None = None) -> FullSetList:
        command = f"FULLSETLIST {self.login}"
        if page:
            command += f" -page {page}"
        if line:
            command += f" -line {line}"
        res = self._api.command(command)
        return validate(res, FullSetList).result

    def TwoSendCardSet(self, app_id: int, sets: int, trade_url: str) -> bool:
        command = f"2SENDCARDSET {self.login} {app_id} {sets} {trade_url}"
        res = self._api.command(command)
        result = validate(res, str).result
        if "sent Success" in result:
            return True
        return False
