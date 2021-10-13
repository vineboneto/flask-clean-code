from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    verify_jwt_in_request,
    get_jwt,
)


class JwtAdapter:
    async def access_token(self, account):
        digest = create_access_token(identity=account)
        return digest

    async def refresh_token(self, account):
        digest = create_refresh_token(identity=account)
        return digest

    async def verify_token(self):
        verify_jwt_in_request()

    async def get_current_user(self):
        return get_jwt()["sub"]
