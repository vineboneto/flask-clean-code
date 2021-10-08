from src.domain.contracts.account.update_account_repo import UpdateAccountRepo
from src.domain.models import Account
from src.domain.contracts import UpdateAccountRepo
from src.application.controllers import Controller
from src.application.validator import Validator


class UpdateAccountController(Controller):
    update_account_repo: UpdateAccountRepo
    validator: Validator

    def __init__(self, update_account_repo: UpdateAccountRepo, validator: Validator):
        super().__init__(validator)
        self.update_account_repo = update_account_repo

    async def perform(self, request) -> Account:
        data = await self.update_account_repo.update(request)
        return self.ok(data)
