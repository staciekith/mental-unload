import os
from dotenv import load_dotenv
from app import create_app, db
import config

load_dotenv()

flask_env = os.environ.get('FLASK_ENV')
match flask_env:
    case 'production':
        config_object = config.Prod
    case 'development':
        config_object = config.Dev
    case 'test':
        config_object = config.Test
    case _:
        config_object = config.Config

app = create_app(config_object)