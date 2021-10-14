from src.application.controllers import LoginController
from src.infra.schema_validator import SchemaAdapter, schema_login
from src.main.factories import make_jwt_adapter, make_repo_account, make_password_hash


def make_login_controller() -> LoginController:
    return LoginController(
        make_jwt_adapter(),
        make_password_hash(),
        make_repo_account(),
        SchemaAdapter(schema_login),
    )
