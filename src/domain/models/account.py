from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    login: str
    username: str
    password: str
