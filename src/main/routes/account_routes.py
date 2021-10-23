from flask import Flask
import src.main.factories.controllers as factories
from src.main.adapters import auth, adapter_route as adapt

create = adapt(factories.make_add_account_controller())
load_by_id = adapt(factories.make_load_account_by_id_controller())
update = adapt(factories.make_update_account_controller())
delete = adapt(factories.make_delete_account_controller())
refresh_token = adapt(factories.make_refresh_token_controller())
login = adapt(factories.make_login_controller())
filter_account = adapt(factories.make_filter_account_controller())


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts/login", "login", login, methods=["POST"])
    app.add_url_rule("/accounts/refresh", "refresh", refresh_token, methods=["POST"])
    app.add_url_rule("/accounts", "create", create, methods=["POST"])
    app.add_url_rule("/accounts/<id>", "load_by_id", auth(load_by_id), methods=["GET"])
    app.add_url_rule("/accounts", "filter_account", auth(filter_account), methods=["GET"])
    app.add_url_rule("/accounts/<id>", "update", auth(update), methods=["PUT"])
    app.add_url_rule("/accounts/<id>", "delete", auth(delete), methods=["DELETE"])
    return app
