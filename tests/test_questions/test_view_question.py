import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.get_question_fixtures import (
    get_question_query,
    get_question_query_response,
    get_paginated_question,
    get_paginated_question_query_response,
    get_paginated_question_invalid_page,
    all_questions_query,
    all_questions_query_response,
    paginated_all_questions_query,
    paginated_all_questions_query_response,
    get_question_by_id_query,
    get_question_by_id_query_response,
    get_question_invalid_id_query,
)

sys.path.append(os.getcwd())


class TestQueryQuestion(BaseTestCase):

    def test_question_query(self):
        """
        Testing for viewing feedback question

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_question_query,
            get_question_query_response
        )

    def test_paginated_question_query(self):
        """
        Testing for paginated result of feedback
        question response
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_paginated_question,
            get_paginated_question_query_response
        )

    def test_paginated_question_invalid_page_query(self):
        """
        Testing for paginated result of feedback
        question response with invalid page
        """
        CommonTestCases.admin_token_assert_in(
            self,
            get_paginated_question_invalid_page,
            "Page does not exist"
        )

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
