import jwt
from flask import current_app, request, jsonify
from functools import wraps
from graphql import GraphQLError
from helpers.database import db_session
from sqlalchemy.exc import SQLAlchemyError
from graphql import GraphQLError

from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole


class Authentication:
    """ Authenicate token and all role based authorization
    :methods
        verify
        decode_token
        user_roles
        auth_required
    """

    def verify(self, token):
        """
        verify token

        :params
            token
        return:
            func|string
        """
        if token:
            return self.decode_token(token)
        return jsonify({
            'message': 'This endpoint requires you to be authenticated.'}), 401

    def decode_token(self, auth_token):
        """
        Decodes the auth token
        :param
            auth_token
        :return
            integer|string
        """
        SECRET_KEY = current_app.config['SECRET_KEY']

        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message': 'Signature expired. Please log in again.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message': 'Invalid token. Please Provied a valid token!'
                }), 401

    def auth_required(self, fn):
        """
        Protects endpoint

        params:
            function
        return:
            function
        """
        def wrapper(*args, **kwargs):
            """ Wrapper function
            takes all the arguments that comes with the incoming function
            makes sure that the end point has a token

            returns:
                func|string
            """
            token = request.headers.get('token')
            validate_token = self.verify(token)
            if type(validate_token) is dict:
                self.save_user(validate_token)
                return fn(*args, **kwargs)
            return validate_token
        return wrapper

    def save_user(self, payload):
        """
        Save user to database.
        
        params: 
            payload: dict
        returns: 
            bloolean
        """
        try:
            email = payload['UserInfo']['email']
            user_data = User.query.filter_by(email=email).first()
            role = Role.query.filter_by(role="User").first()
            if role is None:
                role = Role(role='User')
                role.save()
            if user_data is None:
                user_data = User(email=email)
                user_data.save()
                user_role = UsersRole(user_id=user_data.id, role_id=role.id)
                user_role.save()
            db_session().commit()
        except SQLAlchemyError:
            pass
        return True

    def user_roles(self, *expected_args):
        """ User roles """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                token = request.headers.get('token')
                payload = self.verify(token)
                if type(payload) is dict:
                    email = payload['UserInfo']['email']
                    user_data = User.query.filter_by(email=email).first()
                    user_role = UsersRole.query.filter_by(user_id=user_data.id).first()
                    role = Role.query.filter_by(id=user_role.role_id).first()

                    if role.role in expected_args:
                        return func(*args, **kwargs)
                    else:
                        raise GraphQLError('You are not authorized to perform this action')
                else:
                    raise GraphQLError(payload)
            return wrapper
        return decorator

Auth = Authentication()
