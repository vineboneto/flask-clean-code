from flask_jwt_extended import create_access_token, create_refresh_token


class JwtAdapter:
    async def access_token(self, account):
        digest = create_access_token(identity=account)
        return digest

    async def refresh_token(self, account):
        digest = create_refresh_token(identity=account)
        return digest
