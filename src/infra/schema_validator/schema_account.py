from schema import Schema

schema_add_account = Schema({"username": str, "login": str})

schema_update_account = Schema({"username": str, "id": str, "login": str})
