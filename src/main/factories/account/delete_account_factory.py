from src.application.controllers import DeleteAccountController
from src.main.factories import make_repo_account


def make_delete_account() -> DeleteAccountController:
    return DeleteAccountController(make_repo_account())
