from helpers.database import engine, db_session
from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.update_delete_office_fixture import (
    delete_office_mutation,
    update_office_query,
)
from fixtures.office.office_fixtures import (
    office_mutation_query)


class TestDeleteOffice(BaseTestCase):
    def test_delete_office_without_office_model(self):
        """
        test for unsuccessful floor deletion without office model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE offices CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            delete_office_mutation,
            "does not exist"
        )

    def test_update_office_without_office_model(self):
        """
        test for unsuccessful floor update without office model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE offices CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            update_office_query,
            "does not exist"
        )

    def test_create_office_without_office_model(self):
        """
        test for unsuccessful floor creation without office model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE offices CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            office_mutation_query,
            "does not exist"
        )
