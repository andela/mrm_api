from tests.base import BaseTestCase
from fixtures.room_resource.get_room_resource_fixtures import (
    resource_query, resource_query_response, get_room_resources_by_room_id,
    get_room_resources_by_room_id_response, get_room_resources_by_room_id_error,
    get_room_resources_by_room_id_error_response
)
from helpers.database import db_session
from fixtures.room_resource.get_room_resource_fixtures import (resource_query,  # noqa E501
                                                               resource_query_response,  # noqa E501
                                                               get_room_resources_by_room_id,  # noqa E501
                                                               get_room_resources_by_room_id_response)  # noqa E501

import sys
import os
sys.path.append(os.getcwd())


class TestGetRoomResource(BaseTestCase):

    def test_get_room_resource_list(self):

        execute_query = self.client.execute(
            resource_query,
            context_value={'session': db_session})

        expected_responese = resource_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_get_room_resources_by_room_id_error(self):
        execute_query = self.client.execute(
            get_room_resources_by_room_id_error,
            context_value={'session': db_session})

        expected_responese = get_room_resources_by_room_id_error_response
        self.assertEqual(execute_query, expected_responese)

    def test_get_room_resources_by_room_id(self):

        execute_query = self.client.execute(
            get_room_resources_by_room_id,
            context_value={'session': db_session})

        expected_responese = get_room_resources_by_room_id_response

        self.assertEqual(execute_query, expected_responese)
