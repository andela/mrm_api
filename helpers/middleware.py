from helpers.auth.decode_token import Authentication
from flask import json


class TokenMiddleware(object):
    def resolve(self,next, root, info, **args ):
        return_value = next(root, info, **args)
        token = info.context.headers.get('token')  # get the token from the headers.
        if  token:
            user = Authentication.decode_token(self,auth_token=token) # decode the token from the headers
            user_details = user['UserInfo']
            return user_details
            
            
        else:
            return return_value
        