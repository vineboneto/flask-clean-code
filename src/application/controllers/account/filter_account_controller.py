from src.application.controllers import Controller


class FilterAccountController(Controller):
    def __init__(self, filter_account):
        super().__init__()
        self.filter_account = filter_account

    async def perform(self, request):
        data = await self.filter_account.load_by_fields(request)
        return self.ok(data) if data else self.no_content()
