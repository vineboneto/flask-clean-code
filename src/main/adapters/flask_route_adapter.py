import asyncio
from flask.json import jsonify
from flask.views import View
from src.application.controllers import Controller
from .flask_adapter_request import adapt_request


class AdapterRouter(View):
    def __init__(self, controller: Controller) -> None:
        super().__init__()
        self.controller = controller

    def dispatch_request(self, *args, **kwargs):
        transform_args = adapt_request(kwargs)
        http = asyncio.run(self.controller.handle(transform_args))
        if http.status >= 200 and http.status <= 299:
            return jsonify(http.body), http.status
        return dict(message=http.body.args[0]), http.status


def make_route():
    return AdapterRouter
