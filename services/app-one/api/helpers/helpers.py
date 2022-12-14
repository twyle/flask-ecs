import os
from ..config.config import Config
from dotenv import load_dotenv

load_dotenv()


def set_configuration(app):
    config_name = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(Config[config_name])