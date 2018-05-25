import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client

from tests.base import BaseTestCase
from fixtures.user.user_fixture import (
    user_query, user_query_response,
    query_user_by_email, query_user_email_response
)
from helpers.database import db_session
from api.user.models import User

class TestQueryUser(BaseTestCase):

    def test_query_users(self):
        """
        Testing for User creation
        """
        user = User(email='mrm@andela.com')
        user.save()
        db_session().commit()

        execute_query = self.client.execute(
            user_query,
            context_value={'session': db_session})
        
        expected_responese = user_query_response
        self.assertEqual(execute_query, expected_responese)
    
    def test_query_users_by_email(self):
        user = User(email='mrm@andela.com')
        user.save()
        db_session().commit()

        execute_query = self.client.execute(
            query_user_by_email,
            context_value={'session': db_session})
        
        expected_responese = query_user_email_response
        self.assertEqual(execute_query, expected_responese)

