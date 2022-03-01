from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.adapters.auth0.auth0_adapter import Auth0Adapter

db = SQLAlchemy()
migrate = Migrate(directory='app/adapters/postgres_database/migrations')

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)
    oauth = Auth0Adapter()

    db.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)

    app.constants = {
        'AUTH0_AUDIENCE': config_object.AUTH0_AUDIENCE,
        'AUTH0_API_BASE_URL': config_object.AUTH0_API_BASE_URL,
        'AUTH0_CLIENT_ID': config_object.AUTH0_CLIENT_ID
    }

    with app.app_context():
        app.auth0 = oauth.register_auth0(config_object)

        # Import parts of our application
        from app.adapters.postgres_database import models
        from app.api.event_type_api import event_type_api
        from app.api.event_api import event_api
        from app.api.auth_api import auth_api

        app.register_blueprint(event_type_api)
        app.register_blueprint(event_api)
        app.register_blueprint(auth_api)

        return app