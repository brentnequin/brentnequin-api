from flask_restful import Resource

from app.models import Post
from .schemas import posts_schema

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)
