import asyncio
from flask.json import jsonify
from flask.views import View
from src.application.controllers import Controller
from src.application.middlewares import AuthMiddleware
from .flask_adapter_request import adapt_request


def adapter_middleware(middleware: Controller, view: View):
    def decorator(*args, **kwargs):
        request = adapt_request(kwargs)
        http = asyncio.run(middleware.handle(request))
        if http.status == 403 or http.status == 401:
            return jsonify(http.body), http.status
        return view(*args, **kwargs)

    return decorator


def auth(view: View):
    return adapter_middleware(AuthMiddleware(), view)
