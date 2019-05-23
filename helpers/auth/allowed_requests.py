import os
from flask import request
from graphql import GraphQLError

request_urls = os.environ.get("PROD_REQUEST_URL").split(',')


class RequestAuthentication:

    def validate_origins(self):
        if request.headers['Host'] in request_urls:
            raise GraphQLError(
                "You are not allowed to make requests to this environment")


Request = RequestAuthentication()
