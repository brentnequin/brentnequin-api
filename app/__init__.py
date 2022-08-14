from flask import Flask, render_template
from app.models import db
from app.views import views

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config.py')

db.init_app(app)
app.app_context().push()

app.register_blueprint(views)

# table_row = Post(title="hi how are you")
# db.session.add(table_row)
# db.session.commit()