import sys
import os
sys.path.append(os.getcwd())

from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from helpers.auth.decode_token import Auth
from fixtures.helpers.auth_fixtures import (
    user, token, admin, admin_token, fake_token, expired_token
    )

class TestDecodeToken(BaseTestCase):
    ''' Authenicate token test case '''

    def test_verify_token(self):  
        ''' Verify if token exists '''     
        expected_responese =  b'{\n  "message": "This endpoint requires you to be authenticated."\n}\n'
        self.assertEqual(Auth.verify('')[0].data, expected_responese)

    def test_decode_token(self):
        '''Test Decode token '''
        expected_responese = user
        self.assertEqual(Auth.decode_token(token), expected_responese)

    def test_decode_token_invalid(self):
        ''' Test Decode invalid token '''
        expected_responese = b'{\n  "message": "Invalid token. Please Provied a valid token!"\n}\n'
        self.assertEqual(Auth.decode_token(fake_token)[0].data, expected_responese)

    def test_is_admin(self):
        ''' if user is admin'''
        self.assertEqual(Auth.is_admin(admin_token), True)

    def test_not_admin(self):
        ''' if user is not admin'''
        expected_responese =  b'{\n  "message": "Your can are not authroized to accesst this route."\n}\n'
        self.assertEqual(Auth.is_admin(token)[0].data, expected_responese)
    
    def test_decode_expired_token(self):
        ''' Test Decode expired token '''
        expected_responese = b'{\n  "message": "Signature expired. Please log in again."\n}\n'
        self.assertEqual(Auth.decode_token(expired_token)[0].data, expected_responese)

