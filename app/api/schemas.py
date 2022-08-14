from flask_marshmallow import Marshmallow

from app.models import Post

ma = Marshmallow()

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
        model = Post

posts_schema = PostSchema(many=True)