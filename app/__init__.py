import os

from flask import Flask

from app.models import db
from app.views import views
from app.api.schemas import ma
from app.api import api

rootdir = os.getcwd()

app = Flask(__name__)
app.config.from_pyfile(f'{rootdir}/config.py')

db.init_app(app)
ma.init_app(app)
api.init_app(app)
app.app_context().push()

# table_row = Post(title="hi how are you")
# db.session.add(table_row)
# db.session.commit()

app.register_blueprint(views)