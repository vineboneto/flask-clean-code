from src.domain.contracts import (
    AddAccountRepo,
    LoadAccountByIdRepo,
    UpdateAccountRepo,
    DeleteByIdRepo,
)
from src.domain.models import Account
from src.infra.sql_postgres import AccountModel, db


class AccountRepository(AddAccountRepo, LoadAccountByIdRepo, UpdateAccountRepo):
    async def add(self, params) -> Account:
        account_model = AccountModel(
            username=params.username, login=params.login, password=params.password
        ).create()
        return self.__adapt_account(account_model)

    async def load_by_id(self, id: int) -> Account:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    async def update(self, params) -> Account:
        exist = AccountModel.query.get(params.id)
        if not exist:
            return None
        data = exist.update(username=params.username, login=params.login)
        return self.__adapt_account(data)

    async def delete(self, id: int):
        exist = AccountModel.query.get(id)
        if not exist:
            return None
        data = exist.delete()
        return self.__adapt_account(data)

    def __adapt_account(self, model: AccountModel) -> Account:
        return (
            Account(
                id=model.id, username=model.username, login=model.login, password=model.password
            )
            if model
            else None
        )
