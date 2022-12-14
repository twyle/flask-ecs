import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = True 
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class DevelopmentConfig(BaseConfig):
    """Development confuguration."""
    DEBUG = True 
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class ProductionConfig(BaseConfig):
    """Production configuration."""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


Config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "staging": ProductionConfig,
}
