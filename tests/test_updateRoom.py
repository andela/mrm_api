
from .Basetest import BaseTestCase

class QueryTest(BaseTestCase):
    def test_room_query(self):
        execute_query = self.client.execute(
            '''{ 
            rooms{
                edges{
                    node{
                        id
                        capacity
                        name
                        typeOfRoom
                        }
                    }
                } 
                }
            ''')
        
        assert execute_query == {
  "data": {
    "rooms": {
      "edges": []
    }
  }
}