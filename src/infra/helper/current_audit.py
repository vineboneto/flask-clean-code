import pytz
from datetime import datetime
from src.infra.security import JwtAdapter


class CurrentAudit:
    @staticmethod
    def get_current_date():
        return datetime.now(pytz.timezone("America/Sao_Paulo"))

    @staticmethod
    def get_current_user():
        jwt = JwtAdapter()
        return jwt.get_current_user()
