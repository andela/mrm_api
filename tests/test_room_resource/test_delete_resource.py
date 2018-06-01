import sys
import os


from tests.base import BaseTestCase
from fixtures.room_resource.delete_room_resource import (delete_resource, 
                                                         expected_query_after_delete)
from helpers.database import db_session

sys.path.append(os.getcwd())


class DeleteResource(BaseTestCase):

    def test_deleteresource_mutation(self):

        execute_delete_resource = self.client.execute(
            delete_resource,
            context_value={'session': db_session})
        expected_response = expected_query_after_delete
        self.assertEqual(execute_delete_resource, expected_response)
