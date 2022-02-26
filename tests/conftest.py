import pytest
import config
from app import create_app, db

@pytest.fixture(scope='module')
def app():
    app = create_app(config.Test)

    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def app_db(app):
    db.drop_all()

    with app.app_context():
        yield db

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()