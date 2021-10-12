from typing import Any
from src.application.controllers import Controller


class DeleteAccountController(Controller):
    delete_by_id_account: Any

    def __init__(self, delete_by_id_account):
        super().__init__()
        self.delete_by_id_account = delete_by_id_account

    async def perform(self, request):
        data = await self.delete_by_id_account.delete(request["id"])
        return self.ok(data) if data else self.no_content()
