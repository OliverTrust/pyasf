from pydantic import BaseModel, model_validator


class Cookies(BaseModel):
    browserid: str | None = None
    sessionid: str
    steamLoginSecure: str
    timezoneOffset: str
    steamCountry: str

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: any) -> dict[str, any]:
        lines = data.splitlines()
        d = {}
        for line in lines[2:]:
            d[line.split(":")[0].strip()] = line.split(":")[1].strip()
        return d
