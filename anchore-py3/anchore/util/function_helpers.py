import functools


def trace(f):
    """ Tracing decorator """
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        print('Calling ' + f.__name__ + ' in ' + str(args[0]))
        return f(*args, **kwargs)
    return decorator