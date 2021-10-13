from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.infra.date import get_current_date

db = SQLAlchemy()
migrate = Migrate()


class BaseModel:
    created_at = db.Column("created_at", db.DateTime, nullable=True, default=None)
    updated_at = db.Column("updated_at", db.DateTime, nullable=True, default=None)
    # created_by = db.Column("created_by", db.DateTime, nullable=True, default=None)
    # updated_by = db.Column("updated_by", db.DateTime, nullable=True, default=None)

    def create(self):
        self.created_at = get_current_date()
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **data: dict):
        self.updated_at = get_current_date()
        for k, v in data.items():
            setattr(self, k, v)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self


class AccountModel(db.Model, BaseModel):
    __tablename__ = "Account"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(50), nullable=True)
    login = db.Column("login", db.String(50), unique=True)
    password = db.Column("password", db.String(150), nullable=True)

    def __init__(self, username: str, login: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.login = login
        self.password = password
