from app.exceptions.auth_exception import AuthException
from functools import wraps
from app import auth0
from flask import request
from flask import _request_ctx_stack

def get_token_from_headers(headers):
    auth = headers.get("Authorization", None)

    if None == auth:
        raise AuthException({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected."
        }, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthException({
            "code": "invalid_header",
            "description": "Authorization header must start with 'Bearer '."
        }, 401)

    if len(parts) == 1:
        raise AuthException({
            "code": "invalid_header",
            "description": "Token not found"
        }, 401)

    if len(parts) > 2:
        raise AuthException({
            "code": "invalid_header",
            "description": "Authorization header must be a 'Bearer token'."
        }, 401)

    token = parts[1]

    return token

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_from_headers(request.headers)
        payload = auth0.verify_token(token)
        _request_ctx_stack.top.current_user = payload

        return f(*args, **kwargs)
    return decorated