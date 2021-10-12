from src.domain.models import Account
from src.domain.contracts import DeleteByIdRepo
from src.application.controllers import Controller


class DeleteAccountController(Controller):
    delete_by_id_repo: DeleteByIdRepo

    def __init__(self, delete_by_id_repo: DeleteByIdRepo):
        super().__init__()
        self.delete_by_id_repo = delete_by_id_repo

    async def perform(self, request: Account) -> Account:
        data = await self.delete_by_id_repo.delete(request.id)
        return self.ok(data) if data else self.no_content()
