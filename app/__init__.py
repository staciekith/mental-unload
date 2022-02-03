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

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

from app.adapters.postgres_database import models