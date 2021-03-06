from src.application.controllers import RefreshTokenController
from src.main.factories import make_jwt_adapter


def make_refresh_token_controller():
    return RefreshTokenController(make_jwt_adapter())
