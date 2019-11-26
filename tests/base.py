import os
import sys
import json
import jwt

from flask_testing import TestCase
from graphene.test import Client
from alembic import command, config
from unittest.mock import patch

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.user.models import User
from api.role.models import Role
from fixtures.token.token_fixture import (
    ADMIN_TOKEN, USER_TOKEN, ADMIN_NIGERIA_TOKEN)
from tests.save_test_data import (
    insert_association_tables_data, insert_data_in_database,
    files, association_tables_files
    )

sys.path.append(os.getcwd())


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/mrm'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    @patch('api.room.models.verify_calendar_id')
    def setUp(self, mock_verify_calendar_id):
        app = self.create_app()
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)

            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')

            insert_data_in_database(db_session, files)
            insert_association_tables_data(db_session, association_tables_files)

    def get_admin_location_id(self):
        payload = jwt.decode(ADMIN_TOKEN, verify=False)
        email = payload['UserInfo']['email']
        user = User.query.filter_by(email=email).first()
        location = Location.query.filter_by(name=user.location).first()
        return location.id

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
            db_session.remove()
            Base.metadata.drop_all(bind=engine)


class CommonTestCases(BaseTestCase):
    """Common test cases throught the code.
    This code is used to reduce duplication
    :params
        - admin_token_assert_equal
        - admin_token_assert_in
        - user_token_assert_equal
        - user_token_assert_in
    """

    def admin_token_assert_equal(self, query, expected_response):
        """
        Make a request with admin token and use assertEquals
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def lagos_admin_token_assert_equal(self, query, expected_response):
        """
        Make a request with admin token and use assertEquals
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_NIGERIA_TOKEN}  # noqa E501
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def admin_token_assert_in(self, query, expected_response):
        """
        Make a request with admin token and use assertIn
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def lagos_admin_token_assert_in(self, query, expected_response):
        """
        Make a request with admin token and use assertIn
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_NIGERIA_TOKEN}  # noqa E501
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def user_token_assert_equal(self, query, expected_response):
        """
        Make a request with user token and use assertEquals
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def user_token_assert_in(self, query, expected_response):
        """
        Make a request with user token and use assertIn
        to compare the values
        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def single_structure_query_matches_admin_location(self, query):
        """
        Make a request with admin token to query a structure
        and assert it returns a structure in the admins location
        :params
            - query
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        admin_location_id = self.get_admin_location_id()
        response_data = json.loads(response.data)['data']
        actual_response = response_data['structureByStructureId']
        actual_location_id = actual_response['locationId']
        self.assertEquals(actual_location_id, admin_location_id)

    def structures_query_matches_admin_location(self, query):
        """
        Make a request with admin token to query structures
        and assert it returns structures in the admins location
        :params
            - query
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        admin_location_id = self.get_admin_location_id()
        all_structures = json.loads(response.data)['data']['allStructures']
        for structure in all_structures:
            self.assertEquals(structure['locationId'], admin_location_id)


def change_user_role_helper(func):
    def func_wrapper(self):
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        user = User(email='mrm@andela.com', name='this user',
                    location="Nairobi", picture='www.andela.com/user')
        user.save()
        admin_role = Role.query.filter_by(role='Admin').first()
        user.roles.append(admin_role)
        db_session().commit()
        return headers
    return func_wrapper


def change_test_user_role(func):
    def func_wrapper(self):
        user_role = Role(role='Default User')
        user_role.save()
        user = User(email='mrmtestuser@andela.com', name='Test user',
                    location="Lagos", picture='www.andela.com/testuser')
        user.save()
        user.roles.append(user_role)
        db_session().commit()
    return func_wrapper


def change_user_role_to_super_admin(func):
    def func_wrapper(self):
        super_admin_role = Role.query.filter_by(role='Super Admin').first()
        user = User.query.filter_by(email="peter.walugembe@andela.com").first()
        user.roles.pop()
        user.roles.append(super_admin_role)
        user.save()
        db_session().commit()
        return func(self)
    return func_wrapper
