from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    verify_jwt_in_request,
    get_jwt_identity,
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

    async def verify_refresh_token(self):
        verify_jwt_in_request(refresh=True)
        identity = get_jwt_identity()
        digest = create_access_token(identity=identity)
        return digest

    def get_current_user(self):
        try:
            verify_jwt_in_request()
            return get_jwt()["sub"]["login"] if "sub" in get_jwt() else None
        except Exception as e:
            return None
