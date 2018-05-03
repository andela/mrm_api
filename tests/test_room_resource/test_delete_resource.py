from tests.base import BaseTestCase
from fixtures.room_resource.delete_room_resource import delete_resource, expected_query_after_delete
from helpers.database import db_session
class DeleteResource(BaseTestCase):

    def test_deleteresource_mutation(self):

        execute_delete_resource = self.client.execute(delete_resource)
        self.assertEqual(execute_delete_resource, expected_query_after_delete)