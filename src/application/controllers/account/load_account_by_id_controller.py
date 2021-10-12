from src.domain.contracts import LoadByIdRepo
from src.domain.models import AccountResponse
from src.application.controllers import Controller


class LoadAccountByIdController(Controller):
    load_account_by_id: LoadByIdRepo

    def __init__(self, load_account_by_id: LoadByIdRepo):
        super().__init__()
        self.load_account_by_id = load_account_by_id

    async def perform(self, request) -> AccountResponse:
        data = await self.load_account_by_id.load_by_id(request.id)
        if not data:
            return self.no_content()
        return self.ok(data)
