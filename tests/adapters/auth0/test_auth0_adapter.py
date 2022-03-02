from unittest.mock import Mock
from app.adapters.auth0.auth0_adapter import Auth0Adapter
from config import Test

def test_get_login_url():
    # GIVEN
    auth0_mock = Mock()
    auth0_mock.authorize_redirect.return_value = 'login_url'

    oauth_mock = Mock()
    oauth_mock.register.return_value = auth0_mock

    config = Test

    auth0_adapter = Auth0Adapter()
    auth0_adapter.oauth = auth0_mock
    auth0_adapter.register_auth0(config)
    auth0_adapter.auth0 = auth0_mock

    # WHEN
    result = auth0_adapter.get_login_url('token_uri')

    # THEN
    assert 'login_url' == result

def test_get_logout_url():
    # GIVEN
    auth0_mock = Mock()
    oauth_mock = Mock()
    oauth_mock.register.return_value = auth0_mock

    config = Test
    config.AUTH0_CLIENT_ID = 'client_id'
    config.AUTH0_API_BASE_URL = 'base_url'

    auth0_adapter = Auth0Adapter()
    auth0_adapter.oauth = auth0_mock
    auth0_adapter.register_auth0(config)
    auth0_adapter.auth0 = auth0_mock

    # WHEN
    result = auth0_adapter.get_logout_url('redirect_uri')

    # THEN
    assert 'base_url/v2/logout?returnTo=redirect_uri&client_id=client_id' == result

def test_get_token_from_auth0():
    # GIVEN
    user_info_mock = Mock()
    user_info_mock.json.return_value = {
        'email': 'email'
    }

    auth0_mock = Mock()
    auth0_mock.authorize_access_token.return_value = {
        'access_token': 'token'
    }

    auth0_mock.get.return_value = user_info_mock

    oauth_mock = Mock()
    oauth_mock.register.return_value = auth0_mock

    config = Test

    auth0_adapter = Auth0Adapter()
    auth0_adapter.oauth = auth0_mock
    auth0_adapter.register_auth0(config)
    auth0_adapter.auth0 = auth0_mock

    # WHEN
    result = auth0_adapter.get_token_from_auth0()

    # THEN
    assert {'token': 'token', 'email': 'email'} == result