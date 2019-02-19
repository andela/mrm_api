from tests.base import BaseTestCase, CommonTestCases

from helpers.database import engine, db_session
from fixtures.floor.filter_by_block_fixtures import (
    filter_by_block_query,

)


class TestFilterByBlock(BaseTestCase):
    def test_filter_rooms_in_block_with_database_error(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE floors CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            filter_by_block_query,
            "There seems to be a database connection error"
            )
