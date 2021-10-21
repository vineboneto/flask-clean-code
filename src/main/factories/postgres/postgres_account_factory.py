from src.infra.sql_postgres import AccountRepository, RoleModel


def make_repo_account() -> AccountRepository:
    return AccountRepository()
