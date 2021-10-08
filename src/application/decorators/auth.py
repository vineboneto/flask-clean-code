def auth(f):
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    return decorator
