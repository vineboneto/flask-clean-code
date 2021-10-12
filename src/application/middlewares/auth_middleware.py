from src.application.middlewares import Middleware


class AuthMiddleware(Middleware):
    def __init__(self) -> None:
        super().__init__()

    async def perform(self, request):
        print("Hello World")
        return self.no_content()
