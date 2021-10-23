from src.application.controllers import FilterAccountController
from src.main.factories import make_repo_account


def make_filter_account_controller() -> FilterAccountController:
    return FilterAccountController(make_repo_account())
