from dataclasses import dataclass


@dataclass(frozen=True)
class AccountResponse:
    id: str
    login: str
    username: str
