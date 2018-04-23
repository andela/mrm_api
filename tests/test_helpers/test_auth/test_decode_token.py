import sys
import os
sys.path.append(os.getcwd())

from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from helpers.auth.decode_token import Auth
from fixtures.helpers.auth_fixtures import (
    user, token, admin, admin_token, fake_token
    )

class TestDecodeToken(BaseTestCase):
    ''' Authenicate token test case '''

    def test_verify_token(self):  
        ''' Verify it token exists '''     
        expected_responese = 'Please Provied a valid token!'
        self.assertEqual(Auth.verify(''), expected_responese)

    def test_decode_token(self):
        ''' Decode token '''
        expected_responese = user
        self.assertEqual(Auth.decode_token(token), expected_responese)

    def test_decode_token_ex(self):
        ''' Decode token '''
        expected_responese = 'Invalid token. Please Provied a valid token!'
        self.assertEqual(Auth.decode_token(fake_token), expected_responese)

    def test_is_admin(self):
        ''' if user is admin'''
        self.assertEqual(Auth.is_admin(admin_token), True)

    def test_is_not_admin(self):
        ''' if user is not admin'''
        expected_responese = 'Your can are not authroized to accesst this route.', 401
        self.assertEqual(Auth.is_admin(token), expected_responese)
    
    # def auth_required(self):
