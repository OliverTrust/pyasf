from enum import Enum

from pydantic import BaseModel, model_validator


class LicenseType(Enum):
    COMPLIMENTARY = "Complimentary"
    STEAM_STORE = "Steam Store"
    GIFT_GUEST_PASS = "Gift / GuestPass"
    RETAIL = "Retail"


class License(BaseModel):
    type: LicenseType
    names: list[str]


class Licenses(BaseModel):
    licenses: list[License]

    @classmethod
    def _parse_licenses(
        cls, lines: list[list[str]], license_types: list[str]
    ) -> list[License]:
        licenses = []
        for license_type in license_types:
            names = [line[1] for line in lines if line[0] == license_type]
            if not names:
                continue
            licenses.append(License(type=LicenseType(license_type), names=names))
        return licenses

    @classmethod
    def _validate_license_types(cls, license_types: list[str]) -> None:
        valid_license_types = set(license_type.value for license_type in LicenseType)
        invalid_license_types = set(license_types) - valid_license_types
        if invalid_license_types:
            raise ValueError(
                f"Invalid license types: {', '.join(invalid_license_types)}"
            )

    @model_validator(mode="before")
    @classmethod
    def validate(cls, data: any) -> dict[str, any]:
        lines = [[x.strip() for x in line.split("|")] for line in data.splitlines()[2:]]
        license_types = list(set([line[0] for line in lines]))
        cls._validate_license_types(license_types)
        licenses = cls._parse_licenses(lines, license_types)
        return {"licenses": licenses}
