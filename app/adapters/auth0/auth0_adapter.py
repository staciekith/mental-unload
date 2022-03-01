from typing import Any
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode

class Auth0Adapter:
    oauth: OAuth
    auth0: Any
    config: dict

    def init_app(self, app):
        self.oauth = OAuth()
        self.oauth.init_app(app)

    def register_auth0(self, config) -> Any:
        self.config = config
        self.auth0 = self.oauth.register(
            'auth0',
            client_id=config.AUTH0_CLIENT_ID,
            client_secret=config.AUTH0_CLIENT_SECRET,
            api_base_url=config.AUTH0_API_BASE_URL,
            access_token_url=config.AUTH0_API_BASE_URL + '/oauth/token',
            authorize_url=config.AUTH0_API_BASE_URL + '/authorize',
            client_kwargs={
                'scope': 'openid profile email'
            }
        )

    def get_login_url(self, token_uri):
        return self.auth0.authorize_redirect(
        redirect_uri=token_uri,
        audience=self.config.AUTH0_AUDIENCE)

    def get_logout_url(self, redirect_uri):
        params = {
            'returnTo': redirect_uri,
            'client_id': self.config.AUTH0_CLIENT_ID
        }

        return self.config.AUTH0_API_BASE_URL + '/v2/logout?' + urlencode(params)

    def get_token_from_auth0(self):
        response = self.auth0.authorize_access_token()
        jwt = response['access_token']
        user_info = self.auth0.get('userinfo').json()

        result = {
            'token': jwt,
            'email': user_info['email']
        }

        return result
