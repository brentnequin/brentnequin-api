import pytest

from app.api.resources import PostListResource
from app.models import Post
from app import db

@pytest.fixture()
def post_entry():

    post = Post(title="test")
    db.session.add(Post(title="test"))
    db.session.commit()

    yield post

    Post.query.filter_by(id=post.id).delete()
    db.session.commit()
    
def test_post_list_resource(app):

    post_list_resource = PostListResource()
    post_list = post_list_resource.get()
    print(post_list)
