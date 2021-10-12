from flask import Flask
from flask_jwt_extended import JWTManager


def setup_jwt(app: Flask) -> Flask:
    jwt = JWTManager()
    jwt.init_app(app)
    return app
