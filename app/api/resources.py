from flask import request
from flask_restful import Resource

import json

from app import db
from app.models import Post
from .schemas import posts_schema, post_schema

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

class PostResource(Resource):

    def get(self, id):
        post = Post.query.filter_by(id=id).first()
        return post_schema.dump(post)

    def post(self, id=None):
        try:
            title = request.form['title']
            content = request.form['content']

            post = Post(title=title, content=content)

            db.session.add(post)
            db.session.commit()
        except Exception as e:
            return {"message": str(e)}, 400
        else:
            return None, 200