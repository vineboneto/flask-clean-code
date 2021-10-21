from schema import Schema

schema_add_account = Schema(
    {"username": str, "login": str, "password": str, "roles": [str]}, ignore_extra_keys=True
)

schema_update_account = Schema(
    {"id": str, "username": str, "login": str, "roles": [str]}, ignore_extra_keys=True
)

schema_login = Schema({"login": str, "password": str}, ignore_extra_keys=True)
