from src.infra.security import PasswordHash


def make_password_hash() -> PasswordHash:
    return PasswordHash()
