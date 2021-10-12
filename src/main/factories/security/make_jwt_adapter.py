from src.infra.security.jwt_adapter import JwtAdapter


def make_jwt_adapter() -> JwtAdapter:
    return JwtAdapter()
