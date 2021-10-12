from typing import Any
from src.application.controllers import Controller
from src.application.validator import Validator


class UpdateAccountController(Controller):
    update_account: Any
    validator: Validator
    load_account_by_id: Any

    def __init__(self, update_account, load_account_by_id, validator: Validator):
        super().__init__(validator)
        self.update_account = update_account
        self.load_account_by_id = load_account_by_id

    async def perform(self, request):
        # if account and request.id != account.id and request.login == account.login:
        #     return self.conflict(f"Already exist {request.login}")
        data = await self.update_account.update(request)
        return self.ok(data) if data else self.no_content()
