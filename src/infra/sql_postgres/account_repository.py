from src.infra.sql_postgres import AccountModel, RoleModel, QueryBuilder as query_builder
from src.infra.helper import Checker as check


class AccountRepository:
    async def add(self, params) -> dict:
        account_model = AccountModel(
            username=params["username"],
            login=params["login"],
            password=params["password"],
            roles=self.__get_roles(params["roles"]),
        ).create()
        return self.__adapt_account(account_model)

    async def update(self, params) -> dict:
        account_model = AccountModel.query.get(params["id"])
        if not account_model:
            return None
        data = account_model.update(
            username=params["username"],
            login=params["login"],
            roles=self.__get_roles(params["roles"]),
        )
        return self.__adapt_account(data)

    async def delete(self, id: int) -> dict:
        exist = AccountModel.query.get(id)
        if not exist:
            return None
        data = exist.delete()
        return self.__adapt_account(data)

    async def load_by_login(self, login: str) -> dict:
        account_model = AccountModel.query.filter_by(login=login).first()
        if account_model:
            return self.__adapt_account(account_model)
        return None

    async def load_with_password(self, login: str) -> dict:
        model = AccountModel.query.filter_by(login=login).first()
        if model:
            return dict(
                id=model.id, username=model.username, login=model.login, password=model.password
            )
        return None

    async def load_by_id(self, id: int) -> dict:
        account_model = AccountModel.query.get(id)
        return self.__adapt_account(account_model)

    async def load_by_fields(self, values: dict) -> dict:
        query = (
            query_builder.select(AccountModel)
            .these_values(values)
            .these_fields(["id", "username", "login"])
            .run()
        )
        account_models = (
            query.order_by(AccountModel.id)
            .offset(check.of(values).exist("skip"))
            .limit(check.of(values).exist("take"))
            .all()
        )
        count = query.count()
        return self.__adapt_accounts(account_models, count)

    async def check_login(self, value) -> bool:
        exist = AccountModel.query.filter_by(login=value).first()
        if exist:
            return True
        return False

    def __get_roles(self, account_roles):
        roles = [RoleModel().get_or_create(name=role) for role in account_roles]
        return roles

    def __adapt_accounts(self, models: list[AccountModel], count: int):
        return (
            dict(data=[self.__adapt_account(model) for model in models], count=count)
            if models
            else None
        )

    def __adapt_account(self, model: AccountModel) -> dict:
        return (
            dict(
                id=model.id,
                username=model.username,
                login=model.login,
                roles=[role.name for role in model.roles],
            )
            if model
            else None
        )
