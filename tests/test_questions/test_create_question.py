import sys
import os
from tests.base import BaseTestCase, CommonTestCases
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
