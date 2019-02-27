import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.get_question_fixtures import (
    all_questions_query,
    all_questions_query_response,
    paginated_all_questions_query,
    paginated_all_questions_query_response,
    get_question_by_id_query,
    get_question_by_id_query_response,
    get_question_invalid_id_query,
    get_all_questions_query,
    get_all_questions_query_response
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

    def test_get_all_questions_query(self):
        """
        Test getting all questions
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_all_questions_query,
            get_all_questions_query_response
        )
