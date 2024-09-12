from pydantic import BaseModel, model_validator


class Cookies(BaseModel):
    browserid: str
    sessionid: str
    steamLoginSecure: str
    timezoneOffset: str

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: any) -> dict[str, any]:
        lines = data.splitlines()
        return {
            "browserid": lines[2].split(":")[1].strip(),
            "sessionid": lines[3].split(":")[1].strip(),
            "steamLoginSecure": lines[4].split(":")[1].strip(),
            "timezoneOffset": lines[5].split(":")[1].strip(),
        }
