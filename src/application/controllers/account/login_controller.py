from src.application.controllers import Controller
from src.application.validator import Validator
from werkzeug.security import check_password_hash


class LoginController(Controller):
    def __init__(self, jwt, password_hash, load_account, validator: Validator):
        super().__init__(validator)
        self.jwt = jwt
        self.password_hash = password_hash
        self.load_account = load_account

    async def perform(self, request):
        account = await self.load_account.load_by_login_with_password(request["login"])
        if account:
            is_valid = await self.password_hash.check_password(
                account["password"], request["password"]
            )
            if not is_valid:
                return self.unauthorized()
            token = await self.jwt.access_token(account)
            refresh_token = await self.jwt.refresh_token(account)
            account = {
                **account,
                "token": token,
                "refresh_token": refresh_token,
            }
            del account["password"]
            return self.ok(account)

        return self.unauthorized()
