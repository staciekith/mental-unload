from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
migrate = Migrate(directory='app/adapters/postgres_database/migrations')
oauth = OAuth()

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)

    app.constants = {
        'AUTH0_AUDIENCE': config_object.AUTH0_AUDIENCE,
        'AUTH0_API_BASE_URL': config_object.AUTH0_API_BASE_URL,
        'AUTH0_CLIENT_ID': config_object.AUTH0_CLIENT_ID
    }

    with app.app_context():
        auth0 = oauth.register(
            'auth0',
            client_id=config_object.AUTH0_CLIENT_ID,
            client_secret=config_object.AUTH0_CLIENT_SECRET,
            api_base_url=config_object.AUTH0_API_BASE_URL,
            access_token_url=config_object.AUTH0_API_BASE_URL + '/oauth/token',
            authorize_url=config_object.AUTH0_API_BASE_URL + '/authorize',
            client_kwargs={
                'scope': 'openid profile email',
            },
        )
        app.auth0 = auth0

        # Import parts of our application
        from app.adapters.postgres_database import models
        from app.api.event_type_api import event_type_api
        from app.api.event_api import event_api
        from app.api.auth_api import auth_api

        app.register_blueprint(event_type_api)
        app.register_blueprint(event_api)
        app.register_blueprint(auth_api)

        return app