import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.feedback.feedback_creation_fixtures import (
    create_feedback_query,
    create_feedback_response,
    create_feedback_with_no_rating_or_comment_query,
    create_feedback_with_no_rating_or_comment_response,
    create_feedback_with_invalid_rating_query,
    create_feedback_with_invalid_rating_response,
    create_feedback_with_non_existent_room_id_query,
    create_feedback_with_non_existent_room_id_response
)
sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_feedback_creation(self):
        """
        Testing for feedback creation
        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_feedback_query,
            create_feedback_response
        )

    def test_feedback_creation_with_no_rating_or_comment(self):
        """
        Testing for feedback creation with no rating or comment
        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_feedback_with_no_rating_or_comment_query,
            create_feedback_with_no_rating_or_comment_response
        )

    def test_feedback_creation_with_invalid_rating(self):
        """
        Testing for feedback creation with invalid rating value
        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_feedback_with_invalid_rating_query,
            create_feedback_with_invalid_rating_response
        )

    def test_feedback_creation_with_non_existent_room_id(self):
        """
        Testing for feedback creation with non existent room id
        """
        CommonTestCases.user_token_assert_equal(
            self,
            create_feedback_with_non_existent_room_id_query,
            create_feedback_with_non_existent_room_id_response
        )
