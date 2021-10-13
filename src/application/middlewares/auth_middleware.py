from src.application.middlewares import Middleware


class AuthMiddleware(Middleware):
    def __init__(self, jwt) -> None:
        super().__init__()
        self.jwt = jwt

    async def handle(self, request):
        try:
            self.jwt.verify_token()
            return self.no_content()
        except Exception as e:
            print(e)
            return self.forbidden(e)
