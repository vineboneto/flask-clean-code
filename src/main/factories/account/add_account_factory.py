from src.application.controllers import AddAccountController
from src.infra.schema_validator import SchemaAdapter, schema_add_account
from src.main.factories import make_repo_account, make_password_hash


def make_add_account() -> AddAccountController:
    return AddAccountController(
        make_repo_account(),
        make_repo_account(),
        make_password_hash(),
        SchemaAdapter(schema_add_account),
    )
