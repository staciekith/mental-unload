from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.adapters.auth0.auth0_adapter import Auth0Adapter
from app.exceptions.auth_exception import AuthException
from app.api.auth_exception_handler import handle_auth_error

db = SQLAlchemy()
migrate = Migrate(directory='app/adapters/postgres_database/migrations')
auth0 = Auth0Adapter()

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)
    auth0.init_app(app)

    with app.app_context():
        auth0.register_auth0(config_object)

        app.register_error_handler(AuthException, handle_auth_error)

        # Import parts of our application
        from app.adapters.postgres_database import models
        from app.api.event_type_api import event_type_api
        from app.api.event_api import event_api
        from app.api.auth_api import auth_api
        from app.api.documentation_api import documentation_api

        app.register_blueprint(event_type_api)
        app.register_blueprint(event_api)
        app.register_blueprint(auth_api)
        app.register_blueprint(documentation_api)

        return app