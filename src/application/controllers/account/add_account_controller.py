from src.domain.models import AccountResponse
from src.domain.contracts import AddRepo, CheckExistRepo
from src.application.controllers import Controller
from src.application.validator import Validator


class AddAccountController(Controller):
    add_account: AddRepo
    check_exist_login: CheckExistRepo
    validator: Validator

    def __init__(
        self, add_account: AddRepo, check_exist_login: CheckExistRepo, validator: Validator
    ):
        super().__init__(validator)
        self.add_account = add_account
        self.check_exist_login = check_exist_login

    async def perform(self, request) -> AccountResponse:
        exist = await self.check_exist_login.check(request.login)
        if exist:
            return self.conflict(f"Already exist {request.login}")
        data = await self.add_account.add(request)
        return self.ok(data)
