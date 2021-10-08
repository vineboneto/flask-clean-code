from schema import Schema

schema_add_account = Schema({"username": str})

schema_update_account = Schema({"username": str, "id": str})
