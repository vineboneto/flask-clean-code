from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.infra.helper import CurrentAudit as audit

db = SQLAlchemy()
migrate = Migrate()


class Model:

    created_at = db.Column("created_at", db.DateTime, nullable=True, default=None)
    updated_at = db.Column("updated_at", db.DateTime, nullable=True, default=None)
    created_by = db.Column("created_by", db.String(255), nullable=True, default=None)
    updated_by = db.Column("updated_by", db.String(255), nullable=True, default=None)

    def get_or_create(self, **data):
        exist = self.query.filter_by(**data).first()
        if not exist:
            self.__set_attr(data)
            exist = self.create()
        return exist

    def create(self):
        self.created_by = audit.get_current_user()
        self.created_at = audit.get_current_date()
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **data: dict):
        self.updated_at = audit.get_current_date()
        self.updated_by = audit.get_current_user()
        self.__set_attr(data)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def filter_by_queries(self, queries):
        if len(queries) > 0:
            return self.query.filter(*queries).all()
        return self.query.filter().all()

    def __set_attr(self, data):
        for k, v in data.items():
            setattr(self, k, v)


class RoleModel(db.Model, Model):
    __tablename__ = "Role"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(50), unique=True)

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = name


account_roles = db.Table(
    "AccountRole",
    db.Column("id", db.Integer, primary_key=True, autoincrement=True),
    db.Column("role_id", db.Integer, db.ForeignKey("Role.id"), nullable=True),
    db.Column("account_id", db.Integer, db.ForeignKey("Account.id"), nullable=True),
)


class AccountModel(db.Model, Model):
    __tablename__ = "Account"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(50), nullable=True)
    login = db.Column("login", db.String(50), unique=True)
    password = db.Column("password", db.String(150), nullable=True)
    roles = db.relationship("RoleModel", account_roles)

    def __init__(
        self, username: str = None, login: str = None, password: str = None, roles: list = []
    ) -> None:
        super().__init__()
        self.username = username
        self.login = login
        self.password = password
        self.roles = roles
