from schema import Schema

schema_add_account = Schema(
    {"username": str, "login": str, "password": str}, ignore_extra_keys=True
)

schema_update_account = Schema({"id": str, "username": str, "login": str}, ignore_extra_keys=True)
