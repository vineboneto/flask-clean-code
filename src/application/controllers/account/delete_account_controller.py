from src.domain.models import AccountResponse
from src.domain.contracts import DeleteByIdRepo
from src.application.controllers import Controller


class DeleteAccountController(Controller):
    delete_by_id_account: DeleteByIdRepo

    def __init__(self, delete_by_id_account: DeleteByIdRepo):
        super().__init__()
        self.delete_by_id_account = delete_by_id_account

    async def perform(self, request) -> AccountResponse:
        data = await self.delete_by_id_account.delete(request.id)
        return self.ok(data) if data else self.no_content()
