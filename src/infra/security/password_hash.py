from werkzeug.security import generate_password_hash


class PasswordHash:
    async def hasher(self, password: str):
        digest = generate_password_hash(password)
        return digest
