from src.domain.models import AccountResponse
from src.domain.contracts import AddRepo
from src.application.controllers import Controller
from src.application.validator import Validator


class AddAccountController(Controller):
    add_account: AddRepo
    validator: Validator

    def __init__(self, add_account: AddRepo, validator: Validator):
        super().__init__(validator)
        self.add_account = add_account

    async def perform(self, request) -> AccountResponse:
        data = await self.add_account.add(request)
        return self.ok(data)
