import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'mental-unload-2022-himeboshi')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Prod(Config):
    DEBUG = False

class Dev(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://mental-unload-test:mental-unload-test@localhost/mental-unload-test"