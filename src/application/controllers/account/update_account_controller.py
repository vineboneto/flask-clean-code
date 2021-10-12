from src.domain.contracts import UpdateRepo
from src.domain.models import AccountResponse
from src.application.controllers import Controller
from src.application.validator import Validator


class UpdateAccountController(Controller):
    update_account: UpdateRepo
    validator: Validator

    def __init__(self, update_account: UpdateRepo, validator: Validator):
        super().__init__(validator)
        self.update_account = update_account

    async def perform(self, request) -> AccountResponse:
        data = await self.update_account.update(request)
        return self.ok(data) if data else self.no_content()
