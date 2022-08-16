from app.models import Post

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True

posts_schema = PostSchema(many=True)
post_schema = PostSchema(many=False)