from flask import Flask
from src.main.factories import make_add_account, make_load_account_by_id, make_update_account
from src.main.adapters import make_route, auth


adapt = make_route()

get_by_id = adapt.as_view("acc_by_id", make_load_account_by_id())
create = adapt.as_view("create_acc", make_add_account())
update = adapt.as_view("update_acc", make_update_account())


def set_account_routes(app: Flask) -> Flask:
    app.add_url_rule("/accounts", methods=["POST"], view_func=create)
    app.add_url_rule("/accounts/<id>", methods=["GET"], view_func=auth(get_by_id))
    app.add_url_rule("/accounts/<id>", methods=["PUT"], view_func=update)
    return app
