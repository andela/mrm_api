import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.questions.create_questions_fixtures import (
   create_question_query,
   create_question_response,
   question_mutation_query_without_name,
   create_question_query_with_early_startDate,
   create_question_query_with_early_endDate,
   question_mutation_query_with_invalid_question_type
)


sys.path.append(os.getcwd())


class TestCreateBlock(BaseTestCase):

    def test_question_creation(self):
        """
        Testing for question creation

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            create_question_query,
            create_question_response
        )

    def test_question_creation_with_name_empty(self):
        """
        Test question creation with field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            question_mutation_query_without_name,
            "question_type is required field"
        )

    def test_question_creation_with_invalid_type(self):
        """
        Test question creation with field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            question_mutation_query_with_invalid_question_type,
            "Not a valid question type"
        )

    def test_question_creation_with_wrong_startDate(self):
        """
        Testing for question creation when startDate is
        before current date

        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_question_query_with_early_startDate,
            'startDate should be today or after'
        )

    def test_question_creation_with_wrong_endDate(self):
        """
        Testing for question creation when startDate is
        before current date

        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_question_query_with_early_endDate,
            'endDate should be at least a day after startDate'
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            create_question_query,
            "The database cannot be reached"
            )

    def test_create_question_without_question_model(self):
        """
        test question cannot be created without questions model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE questions CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            create_question_query,
            "does not exist"
        )
