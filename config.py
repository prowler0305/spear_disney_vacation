import os
import datetime

disney_app = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('secret_disney_key', 'mickey_or_donalds')
    PROPAGATE_EXCEPTIONS = True
    THREADED = True
    # PREFERRED_URL_SCHEME = 'https'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = os.environ.get("PORT", 5000)
    HOST = os.environ.get("HOST", "localhost")
    PREFERRED_URL_SCHEME = 'http'


class QaConfig(BaseConfig):
    DEBUG = True
    PORT = os.environ.get("PORT", 8080)
    HOST = os.environ.get("HOST", "0.0.0.0")


class ProductionConfig(BaseConfig):
    DEBUG = False
    PORT = os.environ.get("PORT", 8080)
    HOST = os.environ.get("HOST", "0.0.0.0")
