import os

from flask import Flask

from app.models import db
from app.views import views
from app.api import api

rootdir = os.getcwd()

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile(f'{rootdir}/config.py')

    db.init_app(app)
    api.init_app(app)
    app.app_context().push()

    app.register_blueprint(views)

    return app