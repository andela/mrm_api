import jwt
from flask import request, jsonify


class Authentication:
    """ Authenicate token
    :methods
        decode_token
        get_token
    """

    def get_token(self):
        token = request.headers.get('token')  # get token from headers
        return token

    def decode_token(self):
        """
        Decodes the auth token
        :param
        :return
            integer|string
        """

        try:
            auth_token = self.get_token()
            payload = jwt.decode(auth_token, verify=False)
            return payload['UserInfo']  # Return User Info
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message': 'Signature expired. Please log in again.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message': 'Invalid token. Please Provide a valid token!'
            }), 401


Auth = Authentication()
