from flask_jwt_extended import create_access_token, create_refresh_token


class JwtAdapter:
    def access_token(account):
        digest = create_access_token(identity=account)
        return digest

    def refresh_token(account):
        digest = create_refresh_token(identity=account)
        return digest
