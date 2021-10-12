import src.domain.contracts.repos as Repo
from src.domain.models import AccountResponse
from src.infra.sql_postgres import AccountModel


class AccountRepository(Repo.AddRepo, Repo.LoadByIdRepo, Repo.UpdateRepo, Repo.DeleteByIdRepo):
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

    async def delete(self, id: int):
        exist = AccountModel.query.get(id)
        if not exist:
            return None
        data = exist.delete()
        return self.__adapt_account(data)

    def __adapt_account(self, model: AccountModel) -> AccountResponse:
        return (
            AccountResponse(id=model.id, username=model.username, login=model.login)
            if model
            else None
        )
