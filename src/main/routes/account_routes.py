from flask import Flask
import src.main.factories.controllers as factories
from src.main.adapters import auth, adapter_route

create = adapter_route(factories.make_add_account_controller())
load_by_id = adapter_route(factories.make_load_account_by_id_controller())
update = adapter_route(factories.make_update_account_controller())
delete = adapter_route(factories.make_delete_account_controller())
refresh_token = adapter_route(factories.make_refresh_token_controller())
login = adapter_route(factories.make_login_controller())


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts/login", "login", login, methods=["POST"])
    app.add_url_rule("/accounts/refresh", "refresh", refresh_token, methods=["POST"])
    app.add_url_rule("/accounts", "create", create, methods=["POST"])
    app.add_url_rule("/accounts/<id>", "load_by_id", auth(load_by_id), methods=["GET"])
    app.add_url_rule("/accounts/<id>", "update", auth(update), methods=["PUT"])
    app.add_url_rule("/accounts/<id>", "delete", auth(delete), methods=["DELETE"])
    return app
