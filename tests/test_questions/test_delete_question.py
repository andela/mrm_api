import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.questions.create_questions_fixtures import (
   delete_question_mutation,
   delete_question_response,
   delete_question_invalidId,
   response_for_delete_question_with_database_error
)


sys.path.append(os.getcwd())


class TestDeleteQuestion(BaseTestCase):

    def test_question_delete(self):
        """
        Testing for question update

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_question_mutation,
            delete_question_response
        )

    def test_question_delete_with_invalid_id(self):
        """
        Test question creation with field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_question_invalidId,
            "Question not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_question_mutation,
            "The database cannot be reached"
            )

    def test_delete_question_without_question_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE questions CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_question_mutation,
            response_for_delete_question_with_database_error
        )
