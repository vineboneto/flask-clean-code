import asyncio
from flask.json import jsonify
from src.application.controllers import Controller
from src.main.adapters import adapt_request


def adapter_route(controller: Controller):
    def decorator(*args, **kwargs):
        transform_args = adapt_request(kwargs)
        http = asyncio.run(controller.handle(transform_args))
        if http.status >= 200 and http.status <= 299:
            return jsonify(http.body), http.status
        return dict(message=http.body.args[0]), http.status

    return decorator
