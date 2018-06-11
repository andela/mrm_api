from tests.base import BaseTestCase
from helpers.auth.decode_token import Auth
from fixtures.helpers.auth_fixtures import (user, token, admin_token,
                                            fake_token, expired_token)


class TestDecodeToken(BaseTestCase):
    '''Authenicate token test case'''
    def test_decode_token(self):
        '''Test Decode token '''
        expected_responese = user
        self.assertEqual(Auth.decode_token(token), expected_responese)

    def test_decode_token_invalid(self):
        ''' Test Decode invalid token'''
        expected_responese = b'{\n  "message": "Invalid token. Please Provide a valid token!"\n}\n'  # noqa E501
        self.assertEqual(
            Auth.decode_token(fake_token)[0].data, expected_responese)
    def test_decode_expired_token(self):
        ''' Test Decode expired token '''
        expected_responese = {'Name': 'Joyce', 'UserEmail': 'admin@mrm.com'}
        self.assertEqual(
            Auth.decode_token(expired_token)['UserInfo'], expected_responese)
