import jwt
import os
from flask import request, jsonify


class Authentication():
    """ Authenicate token
      :methods
          verify
          decode_token
          user_credentials
    """

    def verify(self, token):
        """ verify token
          :params token
          :return: func|string
        """

        if token:
            return self.decode_token(token)
        return jsonify(
            {'message': 'This endpoint requires you to be authenticated.'}), 401


    def resolve_token(self, info):
        print(info)
        # auth_header = info.context.META.get('HTTP_AUTHORIZATION')

    def decode_token(self, auth_token):
        """ Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        SECRET_KEY = os.getenv('SECRET_KEY')
        try:
            payload = jwt.decode(auth_token, verify=False)
            print(payload)
            return payload
        except jwt.ExpiredSignatureError:
            return jsonify(
                {'message': 'Signature expired. Please log in again.'}), 401

        except jwt.InvalidTokenError:
            return jsonify(
                {'message': 'Invalid token. Please Provide a valid token!'}), 401  # noqa E501

    def user_credentials(self, token):
        value = self.verify(token)
        if isinstance(value, dict):
            user_email = value['UserInfo']['email']
            nme = value['UserInfo']['name']
            res = {'UserEmail': user_email, 'Name': nme}
            return jsonify(res)
        else:
            return value

    def auth_required(self, fn):
        """ Protects endpoint
           :params: function
           :return: function
        """
        def wrapper(*args, **kwargs):
            """ Wrapper function
              takes all the arguments that comes with the incoming function
              makes sure that the end point has a token
              :returns: func|string
            """
            token = request.headers.get('token')
            validate_token = self.user_credentials(token)
            if validate_token is True:
                return fn(*args, **kwargs)
            return validate_token
        return wrapper


Auth = Authentication()
