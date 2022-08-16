from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    content = db.Column(db.String)

    def __repr__(self):
        return '<Post %r>' % self.title
