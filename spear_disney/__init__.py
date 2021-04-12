import os

from flask import Flask


def create_app():
    spear_app = Flask(__name__)
    spear_app.config.from_object(os.environ.get('app_env'))

    with spear_app.app_context():
        from . import routes
    return spear_app
