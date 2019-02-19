import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import db_session, engine
from fixtures.wing.wing_fixtures import (
    delete_wing_mutation,
    delete_wing_id_not_found,
    delete_wing_response
)

sys.path.append(os.getcwd())


class TestCreateWing(BaseTestCase):

    def test_wing_deletion(self):
        """
        Testing for wing delete
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            delete_wing_mutation,
            delete_wing_response
        )

    def test_wing_delete_other_location(self):
        """
        Testing for wing update in other location apart from Lagos
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_wing_mutation,
            "This action is restricted to Lagos Office admin"
        )

    def test_delete_wing_id_notfound(self):
        """
        Testing for wing creation when floor is not found
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            delete_wing_id_not_found,
            "Wing not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_wing_mutation,
            "The database cannot be reached"
            )

    def test_wing_deletion_without_wings_model(self):
        """
        Testing for wing creation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE wings CASCADE")
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            delete_wing_mutation,
            "There seems to be a database connection error"
        )
