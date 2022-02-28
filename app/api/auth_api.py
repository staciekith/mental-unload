from urllib.parse import urlencode
from flask import current_app
from flask import Blueprint
from flask import jsonify
from flask import url_for
from flask import redirect

auth_api = Blueprint('auth_api', __name__)

# Called by Auth0 after the user logs in
@auth_api.route('/auth/callback')
def auth_callback():
    auth0 = current_app.auth0
    response = auth0.authorize_access_token()
    jwt = response['access_token']
    user_info = auth0.get('userinfo').json()

    result = {
        'token': jwt,
        'email': user_info['email']
    }

    return jsonify(result)

@auth_api.route('/auth/login')
def auth_login():
    auth0 = current_app.auth0

    return auth0.authorize_redirect(
        redirect_uri=url_for('auth_api.auth_callback', _external=True),
        audience=current_app.constants['AUTH0_AUDIENCE'])

@auth_api.route('/auth/logout')
def auth_logout():
    params = {
        'returnTo': url_for('auth_api.auth_login', _external=True),
        'client_id': current_app.constants['AUTH0_CLIENT_ID']
    }

    return redirect(current_app.constants['AUTH0_API_BASE_URL'] + '/v2/logout?' + urlencode(params))