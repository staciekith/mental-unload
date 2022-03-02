from flask import jsonify
from flask import Response
from app.exceptions.auth_exception import AuthException

def handle_auth_error(ex: AuthException) -> Response:
    response = jsonify(ex.error)
    response.status_code = ex.status_code

    return response