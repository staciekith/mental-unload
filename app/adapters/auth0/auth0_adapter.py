from typing import Any
from urllib.request import urlopen
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlencode
import json
from jose import jwt
from app.exceptions.auth_exception import AuthException

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

    def verify_token(self, token):
        jsonurl = urlopen(self.config.AUTH0_API_BASE_URL + '/.well-known/jwks.json')
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=["RS256"],
                    audience=self.config.AUTH0_AUDIENCE,
                    issuer=self.config.AUTH0_API_BASE_URL + '/'
                )
            except jwt.ExpiredSignatureError:
                raise AuthException({
                    "code": "token_expired",
                    "description": "Token is expired."
                }, 401)
            except jwt.JWTClaimsError:
                raise AuthException({
                    "code": "invalid_claims",
                    "description": "Incorrect claims, please check the audience and issuer."
                }, 401)
            except Exception:
                raise AuthException({
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token."
                    }, 401)

            return payload

        raise AuthException({
            "code": "invalid_header",
            "description": "Unable to find appropriate key."
        }, 401)