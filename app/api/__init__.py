from flask_restful import Api

from .resources import PostListResource

api = Api()

api.add_resource(PostListResource, '/posts')