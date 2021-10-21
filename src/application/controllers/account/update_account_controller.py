from src.application.controllers import Controller
from src.application.validator import Validator


class UpdateAccountController(Controller):
    def __init__(self, update_account, load_account_by_login, validator: Validator):
        super().__init__(validator)
        self.update_account = update_account
        self.load_account_by_login = load_account_by_login

    async def perform(self, request):
        exist = await self.__check_exist_login(request)
        if exist:
            return self.conflict(f"Already exist {request['login']}")
        data = await self.update_account.update(request)
        return self.ok(data) if data else self.no_content()

    async def __check_exist_login(self, request):
        account = await self.load_account_by_login.load_by_login(request["login"])
        if account and int(request["id"]) != account["id"] and request["login"] == account["login"]:
            return True
        return False
