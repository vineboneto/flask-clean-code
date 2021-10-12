from src.infra.sql_postgres import AccountModel

from dataclasses import dataclass


@dataclass(frozen=True)
class AccountResponse:
    id: str
    login: str
    username: str


class AccountRepository:
    async def add(self, params) -> AccountResponse:
        account_model = AccountModel(
            username=params.username, login=params.login, password=params.password
        ).create()
        return self.__adapt_account(account_model)

    async def load_by_id(self, id: int) -> AccountResponse:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    async def update(self, params) -> AccountResponse:
        exist = AccountModel.query.get(params.id)
        if not exist:
            return None
        data = exist.update(username=params.username, login=params.login)
        return self.__adapt_account(data)

    async def delete(self, id: int) -> AccountResponse:
        exist = AccountModel.query.get(id)
        if not exist:
            return None
        data = exist.delete()
        return self.__adapt_account(data)

    async def check(self, value) -> bool:
        exist = AccountModel.query.filter_by(login=value).first()
        if exist:
            return True
        return False

    def __adapt_account(self, model: AccountModel) -> AccountResponse:
        return (
            AccountResponse(id=model.id, username=model.username, login=model.login)
            if model
            else None
        )
