from distutils.debug import DEBUG
import os
from flask import Flask
from config import Config

def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app