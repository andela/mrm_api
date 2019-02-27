from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query,
)
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,)
from fixtures.room_resource.delete_room_resource import (
  delete_resource,)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoomResourceError(BaseTestCase):
    def test_create_resource_without_resourse_model(self):
        """
        test for unsuccessful resource creation without resource model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            resource_mutation_query,
            "does not exist"
        )

    def test_delete_resource_without_resourse_model(self):
        """
        test for unsuccessful resource deletion without resource model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            delete_resource,
            "does not exist"
        )

    def test_update_resource_without_resourse_model(self):
        """
        test for unsuccessful resource update without resource model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "does not exist"
        )
