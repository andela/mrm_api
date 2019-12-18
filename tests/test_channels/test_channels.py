from tests.base import BaseTestCase, CommonTestCases
from fixtures.channels.channel_fixtures import (
    channels_query
)
from fixtures.channels.channel_responses_fixtures import (
    channels_response
)


class TestChannels(BaseTestCase):
    def test_query_channels(self):
        """
        Test the query to get
        a list of all active notification channels
        """
        CommonTestCases.user_token_assert_equal(
            self,
            channels_query,
            channels_response
        )
