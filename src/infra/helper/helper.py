import pytz
from datetime import datetime
from src.infra.security import JwtAdapter


def get_current_date():
    return datetime.now(pytz.timezone("America/Sao_Paulo"))


def get_current_user():
    jwt = JwtAdapter()
    return jwt.get_current_user()
