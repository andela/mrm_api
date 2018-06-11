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

    def decode_token(self, auth_token):
        """ Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        SECRET_KEY = os.getenv('SECRET_KEY')
        try:
            payload = jwt.decode(auth_token, verify=False)
            
            return payload
        except jwt.ExpiredSignatureError:
            return jsonify(
                {'message': 'Signature expired. Please log in again.'}), 401

        except jwt.InvalidTokenError:
            return jsonify(
                {'message': 'Invalid token. Please Provide a valid token!'}), 401  # noqa E501

Auth = Authentication()
