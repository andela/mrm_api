import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.questions.create_questions_fixtures import (
   create_question_query,
   create_question_response,
   question_mutation_query_without_name
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
