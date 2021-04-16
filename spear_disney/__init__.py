import os
import sys

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from spear_disney.models import db


def create_app():
    spear_app = Flask(__name__)
    spear_app.config.from_object(os.environ.get('app_env'))
    db.init_app(spear_app)
    migrate = Migrate(spear_app, db)
    manager = Manager(spear_app)
    manager.add_command("db", MigrateCommand)
    if "runserver" in sys.argv:
        manager.add_command("runserver", Server(use_debugger=spear_app.config.get("DEBUG"),
                                                threaded=spear_app.config.get("THREADED"),
                                                port=spear_app.config.get("PORT"),
                                                host=spear_app.config.get("HOST"),
                                                use_reloader=spear_app.config.get("USE_RELOADER")))
    with spear_app.app_context():
        from . import routes
    return manager
