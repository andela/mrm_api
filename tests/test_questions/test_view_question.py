import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.get_question_fixtures import (
    get_question_query,
    get_question_query_response
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
