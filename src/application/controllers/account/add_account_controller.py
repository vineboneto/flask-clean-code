from typing import Any
from src.application.controllers import Controller
from src.application.validator import Validator


class AddAccountController(Controller):
    add_account: Any
    check_exist_login: Any
    password_hash: Any
    validator: Validator

    def __init__(self, add_account, check_exist_login, password_hash, validator: Validator):
        super().__init__(validator)
        self.add_account = add_account
        self.check_exist_login = check_exist_login
        self.password_hash = password_hash

    async def perform(self, request):
        exist = await self.check_exist_login.check(request.login)
        if exist:
            return self.conflict(f"Already exist {request.login}")
        new_password_hash = await self.password_hash.hasher(request.password)
        print(new_password_hash)
        request = request._replace(password=new_password_hash)
        data = await self.add_account.add(request)
        return self.ok(data)
