from typing import Any
from authlib.integrations.flask_client import OAuth

class Auth0Adapter:
    oauth: OAuth

    def init_app(self, app):
        self.oauth = OAuth()
        self.oauth.init_app(app)

    def register_auth0(self, config) -> Any:
        return self.oauth.register(
            'auth0',
            client_id=config.AUTH0_CLIENT_ID,
            client_secret=config.AUTH0_CLIENT_SECRET,
            api_base_url=config.AUTH0_API_BASE_URL,
            access_token_url=config.AUTH0_API_BASE_URL + '/oauth/token',
            authorize_url=config.AUTH0_API_BASE_URL + '/authorize',
            client_kwargs={
                'scope': 'openid profile email',
            },
        )