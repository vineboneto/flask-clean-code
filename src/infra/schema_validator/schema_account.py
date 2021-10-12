from schema import Schema

schema_add_account = Schema({"username": str, "login": str, "password": str})

schema_update_account = Schema({"id": str, "username": str, "login": str})
