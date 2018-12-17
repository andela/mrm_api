import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.create_questions_fixtures import (
   delete_question_mutation,
   delete_question_response,
   delete_question_invalidId
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
