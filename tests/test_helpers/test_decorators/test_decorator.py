import sys
import os
sys.path.append(os.getcwd())

from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from helpers.decorators.auth import Auth
from fixtures.helpers.decorators_fixtures import (
    user, token, admin_token, admin, admin_token, fake_token, expired_token,
    query_string, query_string_response,
    user_role_401_msg
    )
from sqlalchemy.exc import SQLAlchemyError
from helpers.database import db_session

from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole


class TestDecodeToken(BaseTestCase):
    ''' Authenicate token test case '''

    def test_verify_token(self):  
        ''' Verify if token exists '''     
        expected_responese =  b'{\n  "message": "This endpoint requires you to be authenticated."\n}\n'
        self.assertEqual(Auth.verify('')[0].data, expected_responese)
    
    def test_decode_token(self):
        '''Test Decode token '''
        expected_responese = user
        self.assertEqual(Auth.verify(token), expected_responese)

    def test_decode_token_invalid(self):
        ''' Test Decode invalid token '''
        expected_responese = b'{\n  "message": "Invalid token. Please Provied a valid token!"\n}\n'
        self.assertEqual(Auth.decode_token(fake_token)[0].data, expected_responese)
    
    def test_decode_expired_token(self):
        ''' Test Decode expired token '''
        expected_responese = b'{\n  "message": "Signature expired. Please log in again."\n}\n'
        self.assertEqual(Auth.decode_token(expired_token)[0].data, expected_responese)

    def test_save_user(self):
        ''' Test method saves a user success '''
        expected_responese = True
        self.assertEqual(Auth.save_user(user), expected_responese)

    def test_user_role(self):
        ''' Test method saves a user error '''

        user = User(email="admin@mrm.com")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        db_session().commit()

        query = self.app_test.post(query_string, headers={'token': admin_token})

        expected_response = query_string_response

        self.assertEqual(query.data, expected_response)

    def test_user_role_401(self):
        ''' Test method saves a user error '''

        query = self.app_test.post(query_string, headers={'token': token})

        expected_response = user_role_401_msg
        print(query.data)
        self.assertEqual(query.data, expected_response)
    
    def test_user_role_error(self):
        query = self.app_test.post(query_string, headers={'token': 'stuff'})

        expected_response = b'{\n  "message": "Invalid token. Please Provied a valid token!"\n}\n'
        self.assertEqual(query.data, expected_response)

