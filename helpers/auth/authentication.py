import json
import jwt

from flask import request, jsonify
from functools import wraps

import requests
from graphql import GraphQLError
from sqlalchemy.exc import SQLAlchemyError
from flask_json import JsonError

from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole
from api.notification.models import Notification as NotificationModel

from helpers.database import db_session

api_url = "https://api-prod.andela.com/api/v1/"


class Authentication:
    """ Authenicate token
    :methods
        decode_token
        get_token
    """

    def get_token(self):
        token = request.headers['Authorization'].split()[1]
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
            if auth_token is None:
                return jsonify({
                    'message':
                    'Invalid token. Please Provide a valid token!'
                }), 401

            payload = jwt.decode(auth_token, verify=False)
            self.user_info = payload['UserInfo']
            return payload['UserInfo']
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message': 'Signature expired. Please log in again.'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message':
                'Invalid token. Please Provide a valid token!'
            }), 401

    def save_user(self):
        """
        Save user to database.

        params:
            user_info: dict
        returns:
            bloolean
        """
        try:
            email = self.user_info['email']
            name = self.user_info['name']
            picture = self.user_info['picture']
            user = User.query.filter_by(email=email).first()
            role = Role.query.filter_by(role='Default User').first()
            if not role:
                role = Role(role='Default User')
                role.save()

            if not user:
                try:
                    user_data = User(email=email, name=name, picture=picture)
                    user_data.save()
                    user_role = UsersRole(
                        user_id=user_data.id, role_id=role.id)
                    user_role.save()
                    notification_settings = NotificationModel(
                        user_id=user_data.id)
                    notification_settings.save()
                except Exception as e:  # noqa
                    db_session.rollback()
        except SQLAlchemyError:
            pass
        return True

    def user_roles(self, *expected_args):
        """ User roles """

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                user_data = self.decode_token()
                if type(user_data) is dict:
                    self.save_user()
                    email = user_data['email']
                    user = User.query.filter_by(email=email).first()
                    headers = {"Authorization": 'Bearer ' + self.get_token()}
                    data = requests.get(
                        api_url + "users?email=%s" % user.email,
                        headers=headers)
                    response = json.loads(data.content.decode("utf-8"))
                    if response['values'][0]['location']:
                        user.location = \
                            response['values'][0]['location']['name']
                        user.save()
                    else:
                        user.location = "Nairobi"
                        user.save()
                    user_role = UsersRole.query.filter_by(
                        user_id=user.id).first()
                    role = Role.query.filter_by(id=user_role.role_id).first()

                    if role.role in expected_args:
                        return func(*args, **kwargs)
                    else:
                        res = 'You are not authorized to perform this action'
                        if 'REST' in expected_args:
                            raise JsonError(message=res, status=401)
                        raise GraphQLError(res)
                else:
                    raise GraphQLError(user_data[0].data)

            return wrapper

        return decorator


Auth = Authentication()
