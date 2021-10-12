from typing import Any
from src.application.controllers import Controller


class LoadAccountByIdController(Controller):
    load_account_by_id: Any

    def __init__(self, load_account_by_id):
        super().__init__()
        self.load_account_by_id = load_account_by_id

    async def perform(self, request):
        data = await self.load_account_by_id.load_by_id(request.id)
        if not data:
            return self.no_content()
        return self.ok(data)
