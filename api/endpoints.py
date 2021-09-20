# Copyright 2021 Nathan Conroy. All rights reserved.
"""
This module contains all the server's endpoints.
"""

import http.client as http_client

from flask_restx import Resource, Api
from flask import Flask


TEST_ROUTE = '/test'
POSTS_ROUTE = '/posts'


app = Flask(__name__)
api = Api(app)


@api.route(TEST_ROUTE)
class Test(Resource):
    """
    An endpoint that serves to merely test
    that the Flask server works.
    """
    def get(self):
        return http_client.OK


@api.route(POSTS_ROUTE)
class Posts(Resource):
    """
    Responds with all the blog's posts.
    """
    def get(self):
        return http_client.OK
