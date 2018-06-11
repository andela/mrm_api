from helpers.auth.decode_token import Authentication
from flask import jsonify


class TokenMiddleware(object):
    def resolve(self,next, root, info, **args ):
        return_value = next(root, info, **args)
        token = info.context.headers.get('token')  # get the token from the headers.
        user = Authentication.decode_token(self,auth_token=token) # decode the token from the headers
        if  token:
            useremail = user['UserInfo']['email']
            userename = user['UserInfo']['name']
            return return_value
        else:
            return return_value
        