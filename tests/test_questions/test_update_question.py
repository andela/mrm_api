import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.create_questions_fixtures import (
   update_question_mutation,
   update_question_response,
   update_question_invalidId
)


sys.path.append(os.getcwd())


class TestUpdateQuestion(BaseTestCase):

    def test_question_update(self):
        """
        Testing for question update

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_question_mutation,
            update_question_response
        )

    def test_question_update_with_invalid_id(self):
        """
        Test question creation with field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_question_invalidId,
            "Question not found"
        )
