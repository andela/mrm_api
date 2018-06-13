import jwt

from flask import request, jsonify
from functools import wraps
from graphql import GraphQLError
from sqlalchemy.exc import SQLAlchemyError

from api.user.models import User
from api.roles.models import Role
from api.user_role.models import UsersRole
from helpers.auth.user_details import get_user_details


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
    
    def save_user(self, user_info):
        """
        Save user to database.
        
        params: 
            user_info: dict
        returns: 
            bloolean
        """
        try:
            email = user_info['email']
            user = User.query.filter_by(email=email).first()
            role = Role.query.filter_by(role='Default User').first()
            if not role:
                role = Role(role='Default User')
                role.save()
            if not user:
                user_data = User(email=email, location=user_info['location'])
                user_data.save()
                user_role = UsersRole(user_id=user_data.id, role_id=role.id)
                user_role.save()
        except SQLAlchemyError:
            pass
        return True
    
    def user_roles(self, *expected_args):
        """ User roles """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                user_data = self.decode_token()
                if user_data:
                    user_info = get_user_details(self.get_token(),
                                                 user_data['id'])
                    self.save_user(user_info)
                    email = user_data['email']
                    user = User.query.filter_by(email=email).first()
                    user_role = UsersRole.query.filter_by(user_id=user.id).first()
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
