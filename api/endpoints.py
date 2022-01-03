# Copyright 2021 Nathan Conroy. All rights reserved.
"""
This module contains all the server's endpoints.
"""

import http.client as http_client

from flask_restx import Resource, Api
from flask_cors import CORS
from flask import Flask

from content.fetch import fetch_posts


TEST_ROUTE = '/test'
POSTS_ROUTE = '/posts'
ABOUT_ROUTE = '/about'


app = Flask(__name__)
CORS(app)
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
        return fetch_posts()


@api.route(ABOUT_ROUTE)
class About(Resource):
    """
    *** UNDER DEVELOPMENT - NOT READY FOR PROD USE ***

    Responds with about page.
    """
    def get(self):
        return http_client.OK
