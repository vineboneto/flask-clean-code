from src.domain.contracts import AddAccountRepo, LoadAccountByIdRepo, UpdateAccountRepo
from src.domain.models import Account
from src.infra.sql_postgres import AccountModel


class AccountRepository(AddAccountRepo, LoadAccountByIdRepo, UpdateAccountRepo):
    async def add(self, params) -> Account:
        account_model = AccountModel(username=params.username).create()
        return self.__adapt_account(account_model)

    async def load_by_id(self, id: int) -> Account:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    async def update(self, params) -> Account:
        account_model = AccountModel.query.get(params.id)
        return self.__adapt_account(account_model)

    def __adapt_account(self, model: AccountModel) -> Account:
        return Account(id=model.id, username=model.username) if model else None
