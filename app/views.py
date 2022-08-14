from flask import Blueprint, render_template, session, abort

from .models import Post

views = Blueprint('views', __name__)

@views.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@views.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)