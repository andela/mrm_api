import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.user_response_fixtures import (
   create_rate_query,
   create_rate_response,
   rate_wrong_question,
   invalid_rating_number,
   rate_with_non_existent_room
)
from fixtures.response.user_response_check import (
    check_non_existing_question,
    check_with_non_existent_room,
    select_check_question
)
from fixtures.response.user_response_suggestions import (
    create_suggestion_question,
    create_suggestion_question_response,
    make_suggestion_in_non_existent_room,
    make_suggestion_on_wrong_question,
    choose_non_existent_question
)


sys.path.append(os.getcwd())


class TestCreateResponse(BaseTestCase):

    def test_create_rate(self):
        """
        Testing for creating rates

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_rate_query,
            create_rate_response
        )

    def test_rate_wrong_question(self):
        """
        Testing for rating wrong question

        """
        CommonTestCases.user_token_assert_in(
            self,
            rate_wrong_question,
            "Select a rating question"
        )

    def test_invalid_rating_number(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            invalid_rating_number,
            "Please rate between 1 and 5"
        )

    def test_rate_non_existent_room(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            rate_with_non_existent_room,
            "Non-existent room id"
        )

    def test_check_wrong_question(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            check_non_existing_question,
            "Question does not exist"
        )

    def test_check_non_existent_room(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            check_with_non_existent_room,
            "Non-existent room id"
        )

    def test_create_check(self):
        """
        Testing for creating rates

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_rate_query,
            create_rate_response
        )

    def test_answer_right_question(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            select_check_question,
            "Select a check question"
        )

    def test_create_suggestion(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_suggestion_question,
            create_suggestion_question_response
        )

    def test_suggestion_on_non_existent_room(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            make_suggestion_in_non_existent_room,
            "Non-existent room id"
        )

    def test_suggestion_on_wrong_question(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            make_suggestion_on_wrong_question,
            "Select the correct question"
        )

    def test_suggestion_on_non_existent_question(self):
        """
        Testing for invalid rating number

        """
        CommonTestCases.user_token_assert_in(
            self,
            choose_non_existent_question,
            "Question does not exist"
        )
