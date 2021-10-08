from src.application.controllers import UpdateAccountController
from src.main.factories import make_repo_account
from src.infra.schema_validator import SchemaAdapter, schema_update_account


def make_update_account() -> UpdateAccountController:
    return UpdateAccountController(make_repo_account(), SchemaAdapter(schema_update_account))
