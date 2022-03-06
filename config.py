import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'mental-unload-2022-himeboshi')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_DATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET')
    AUTH0_API_BASE_URL = os.getenv('AUTH0_API_BASE_URL')
    AUTH0_AUDIENCE = os.getenv('AUTH0_AUDIENCE')

class Prod(Config):
    print(os.getenv('PORT'))
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1) if os.getenv('DATABASE_URL').startswith("postgres://") else os.getenv('DATABASE_URL')

class Dev(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://mental-unload-test:mental-unload-test@postgresql-test/mental-unload-test"
    AUTH0_CLIENT_ID = ''
    AUTH0_CLIENT_SECRET = ''
    AUTH0_API_BASE_URL = ''
    AUTH0_AUDIENCE = ''