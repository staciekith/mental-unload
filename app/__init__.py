from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(directory='app/adapters/postgres_database/migrations')

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import parts of our application
        from app.adapters.postgres_database import models
        from app.api.event_type_api import event_type_api
        from app.api.event_api import event_api

        app.register_blueprint(event_type_api)
        app.register_blueprint(event_api)

        return app