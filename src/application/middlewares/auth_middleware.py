from src.application.controllers import Controller


class AuthMiddleware(Controller):
    def __init__(self) -> None:
        super().__init__()

    async def perform(self, request):
        print("Hello World")
        return self.no_content()
