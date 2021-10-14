from src.infra.sql_postgres import AccountModel


class AccountRepository:
    def __init__(self) -> None:
        pass

    async def add(self, params) -> dict:
        account_model = AccountModel(
            username=params["username"], login=params["login"], password=params["password"]
        ).create()
        return self.__adapt_account(account_model)

    async def load_by_login(self, login: str) -> dict:
        account_model = AccountModel.query.filter_by(login=login).first()
        if account_model:
            return self.__adapt_account(account_model)
        return None

    async def load_by_login_with_password(self, login: str) -> dict:
        model = AccountModel.query.filter_by(login=login).first()
        if model:
            return dict(
                id=model.id, username=model.username, login=model.login, password=model.password
            )
        return None

    async def load_by_id(self, id: int) -> dict:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    async def update(self, params) -> dict:
        exist = AccountModel.query.get(params["id"])
        if not exist:
            return None
        data = exist.update(username=params["username"], login=params["login"])
        return self.__adapt_account(data)

    async def delete(self, id: int) -> dict:
        exist = AccountModel.query.get(id)
        if not exist:
            return None
        data = exist.delete()
        return self.__adapt_account(data)

    async def check_login(self, value) -> bool:
        exist = AccountModel.query.filter_by(login=value).first()
        if exist:
            return True
        return False

    def __adapt_account(self, model: AccountModel) -> dict:
        return dict(id=model.id, username=model.username, login=model.login) if model else None
