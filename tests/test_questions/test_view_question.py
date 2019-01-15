import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.get_question_fixtures import (
    get_question_query,
    get_question_query_response,
    get_paginated_question,
    get_paginated_question_query_response,
    get_paginated_question_invalid_page,
)
from fixtures.questions.create_questions_fixtures import (
    all_questions_query,
    all_questions_response
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
        Testing for viewing feedback question

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            all_questions_query,
            all_questions_response
        )
