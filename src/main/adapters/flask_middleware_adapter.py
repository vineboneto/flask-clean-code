import asyncio
from flask.json import jsonify
from flask.views import View
from src.application.middlewares import Middleware
from src.main.factories import make_auth_middleware
from src.main.adapters import adapt_request


def adapter_middleware(middleware: Middleware, view: View):
    def decorator(*args, **kwargs):
        request = adapt_request(kwargs)
        http = asyncio.run(middleware.handle(request))
        if http.status == 403 or http.status == 401 or http.status == 422:
            return dict(message=http.body.args[0]), http.status
        return view(*args, **kwargs)

    return decorator


def auth(view: View):
    return adapter_middleware(make_auth_middleware(), view)
