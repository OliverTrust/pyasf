from .models.full_set_list import FullSetList
from pyasf import API, validate


class Command:
    def __init__(self, api: API, login: str) -> None:
        self._api = api
        self.login = login

    def fullsetlist(self, page: int | None = None, line: int | None = None) -> FullSetList:
        command = f"FULLSETLIST {self.login}"
        if page:
            command += f" -page {page}"
        if line:
            command += f" -line {line}"
        res = self._api.command(command)
        return validate(res, FullSetList).result
