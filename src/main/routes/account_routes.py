import src.main.factories as factories
from flask import Flask
from src.main.adapters import auth, adapter_route

create = adapter_route(factories.make_add_account())
load_by_id = adapter_route(factories.make_load_account_by_id())
update = adapter_route(factories.make_update_account())
delete = adapter_route(factories.make_delete_account())


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts", "create", create, methods=["POST"])
    app.add_url_rule("/accounts/<id>", "load_by_id", auth(load_by_id), methods=["GET"])
    app.add_url_rule("/accounts/<id>", "update", update, methods=["PUT"])
    app.add_url_rule("/accounts/<id>", "delete", delete, methods=["DELETE"])
    return app
