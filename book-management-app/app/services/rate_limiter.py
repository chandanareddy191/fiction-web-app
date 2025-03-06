from functools import wraps
from flask import request
from flask_limiter.util import get_remote_address
from app import limiter

def limit_login_attempts(f):
    @wraps(f)
    @limiter.limit("5 per minute")
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

def rate_limit_book_routes(routes):
    @wraps(routes)
    @limiter.limit("30 per hour")
    def decorated_function(*args, **kwargs):
        return routes(*args, **kwargs)
    return decorated_function