from flask import Flask
from src.main.factories import make_add_account, make_load_account_by_id, make_update_account
from src.main.adapters import auth, adapter_route

create = adapter_route(make_add_account())
load_by_id = adapter_route(make_load_account_by_id())
update = adapter_route(make_update_account())


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts", "create", create, methods=["POST"])
    app.add_url_rule("/accounts/<id>", "load_by_id", auth(load_by_id), methods=["GET"])
    app.add_url_rule("/accounts/<id>", "update", update, methods=["PUT"])
    return app
