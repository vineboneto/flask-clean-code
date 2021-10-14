from src.application.controllers import Controller
from src.application.validator import Validator


class AddAccountController(Controller):
    def __init__(self, add_account, check_exist_login, password_hash, jwt, validator: Validator):
        super().__init__(validator)
        self.add_account = add_account
        self.check_exist_login = check_exist_login
        self.password_hash = password_hash
        self.jwt = jwt

    async def perform(self, request):
        exist = await self.check_exist_login.check_login(request["login"])
        if exist:
            return self.conflict(f"Already exist {request['login']}")
        new_password_hash = await self.password_hash.hasher(request["password"])
        request = {**request, "password": new_password_hash}
        data = await self.add_account.add(request)
        token = await self.jwt.access_token(request)
        refresh_token = await self.jwt.refresh_token(data)
        data = {**data, "token": token, "refresh_token": refresh_token}
        return self.ok(data)
