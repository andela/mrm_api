import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.questions.get_question_fixtures import (
    all_questions_query,
    all_questions_query_response,
    paginated_all_questions_query,
    paginated_all_questions_query_response,
    get_question_by_id_query,
    get_question_by_id_query_response,
    get_question_invalid_id_query,
    response_for_wrong_migration
)

sys.path.append(os.getcwd())


class TestQueryQuestion(BaseTestCase):

    def test_all_questions_query(self):
        """
        Test getting all questions
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            all_questions_query,
            all_questions_query_response
        )

    def test_paginated_all_questions_query(self):
        """
        Test getting paginated all questions
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            paginated_all_questions_query,
            paginated_all_questions_query_response
        )

    def test_paginated_all_questions_query_with_no_question(self):
        """
        Test getting paginated all questions
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE responses CASCADE")
            conn.execute("DELETE FROM questions CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            paginated_all_questions_query,
            "No questions found"
        )

    def test_get_question_query(self):
        """
        Test getting a question using its id
        """
        CommonTestCases.admin_token_assert_equal(
            self, get_question_by_id_query,
            get_question_by_id_query_response)

    def test_get_question_invalid_id_query(self):
        """
        Testing getting a question while passing an invalid id
        """
        CommonTestCases.admin_token_assert_in(
            self,
            get_question_invalid_id_query,
            "Question does not exist"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_equal(
            self,
            all_questions_query,
            response_for_wrong_migration
            )
