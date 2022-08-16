import os

from flask import Flask

from app.models import db
from app.views import views
from app.api import api

rootdir = os.getcwd()

def create_app(app_config=None):

    app = Flask(__name__)
    app.config.from_object(app_config or 'app.config.Config')

    db.init_app(app)
    api.init_app(app)

    app.register_blueprint(views)

    return app

if __name__ == "__main__":

    app = create_app()
    with app.app_context():
        db.create_all()
    app.run()