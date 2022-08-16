from flask_restful import Api

from .resources import PostListResource, PostResource

api = Api()

api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/post/<int:id>')