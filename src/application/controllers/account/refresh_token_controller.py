from src.application.controllers import Controller


class RefreshTokenController(Controller):
    def __init__(self, jwt):
        super().__init__()
        self.jwt = jwt

    async def perform(self, request):
        token = await self.jwt.verify_refresh_token()
        return self.ok(token=token)
