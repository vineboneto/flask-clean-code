from werkzeug.security import generate_password_hash, check_password_hash


class PasswordHash:
    async def hasher(self, password: str):
        digest = generate_password_hash(password)
        return digest

    async def check_password(self, password_hash: str, password: str):
        is_valid = check_password_hash(password_hash, password)
        return is_valid
