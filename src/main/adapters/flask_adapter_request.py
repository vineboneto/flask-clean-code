from flask.json import request
from collections import namedtuple


def to_namedtuple(current_dict):
    return namedtuple("request", current_dict.keys())(*current_dict.values())


def adapt_request(args_params):
    args_dict = dict()
    if request.json:
        args_dict.update(request.json)
    args_dict.update(request.args.to_dict())
    args_dict.update(args_params)
    transform = to_namedtuple(args_dict)
    return transform
