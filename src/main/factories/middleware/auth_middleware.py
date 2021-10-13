from src.application.middlewares import AuthMiddleware
from src.main.factories import make_jwt_adapter


def make_auth_middleware() -> AuthMiddleware:
    return AuthMiddleware(make_jwt_adapter())
