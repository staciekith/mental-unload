from flask import Blueprint
from flask import jsonify
from flask import url_for
from flask import redirect
from app import auth0

auth_api = Blueprint('auth_api', __name__)

# Called by Auth0 after the user logs in
@auth_api.route('/auth/callback')
def auth_callback():
    result = auth0.get_token_from_auth0()

    return jsonify(result)

@auth_api.route('/auth/login')
def auth_login():
    login_url = auth0.get_login_url(url_for('auth_api.auth_callback', _external=True))

    return login_url

@auth_api.route('/auth/logout')
def auth_logout():
    logout_url = auth0.get_logout_url(url_for('auth_api.auth_login', _external=True))

    return redirect(logout_url)