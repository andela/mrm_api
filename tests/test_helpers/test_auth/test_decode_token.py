import sys
import os
import jwt
sys.path.append(os.getcwd())

from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from helpers.auth.decode_token import Auth
from fixtures.helpers.auth_fixtures import (
    user, token, admin, admin_token, fake_token, expired_token, no_token
    )

class TestDecodeToken(BaseTestCase):
    ''' Authenicate token test case '''

    def test_verify_token(self):  
        ''' Verify if token exists '''     
        expected_responese =  b'{\n  "message": "This endpoint requires you to be authenticated."\n}\n'
        self.assertEqual(Auth.verify('')[0].data, expected_responese)
        print(expired_token)

    def test_decode_token(self):
        '''Test Decode token '''
        expected_responese = user
        self.assertEqual(Auth.decode_token(token), expected_responese)

    def test_decode_token_invalid(self):
        ''' Test Decode invalid token '''
        expected_responese = b'{\n  "message": "Invalid token. Please Provide a valid token!"\n}\n'
        self.assertEqual(Auth.decode_token(fake_token)[0].data, expected_responese)

    def test_user_credentials(self):
        ''' if user is has credentials'''
        response = b'{\n  "Name": "Namuli", \n  "UserEmail": "admin@mrm.com"\n}\n'
        self.assertEqual(Auth.user_credentials(admin_token).data,response )
        
    
    def test_decode_expired_token(self):
        ''' Test Decode expired token '''

        expected_responese = {'Name': 'Joyce', 'UserEmail': 'admin@mrm.com'}
        print(Auth.decode_token(expired_token))
        self.assertEqual(Auth.decode_token(expired_token)['UserInfo'], expected_responese)