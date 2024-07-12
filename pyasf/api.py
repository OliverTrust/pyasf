import httpx
from pydantic import BaseModel, Field


class API:
    def __init__(self, ipc: str = "http://127.0.0.1:1242", password: str | None = None, timeout: float = 120) -> None:
        self._ipc = ipc
        self._password = password
        self.timeout = timeout

    def request(self, method: str, path: str, json: dict | None) -> httpx.Response:
        headers = None
        if self._password:
            headers = {"Authentication": self._password}
        return httpx.request(method, f"{self._ipc}/{path}", json=json, headers=headers, timeout=self.timeout)

    def command(self, command: str) -> httpx.Response:
        path = "api/command"
        body = {"command": command}
        return self.request("POST", path, body)


class Response[ResultT](BaseModel):
    result: ResultT | None = Field(None, alias="Result")
    message: str = Field(..., alias="Message")
    success: bool = Field(..., alias="Success")


def validate[ResultT](response: httpx.Response, result: type[ResultT]) -> Response:
    return Response[result](**response.json())
