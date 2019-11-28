from ..output.OutputBuilder import build
from ..output.Error import error_item

rooms_containing_resource_query = '''
   query {
     roomsContainingResource(resourceId: 1) {
      room {
        name
        capacity
      }
    }
  }
        '''

rooms_containing_resource_expected_response = {
    "data": {
        "roomsContainingResource": [
            {
                "room": {
                    "name": "Entebbe",
                    "capacity": 6
                }
            },
        ]
    }
}

rooms_containing_non_existent_resource_query = '''
   query {
     roomsContainingResource(resourceId: 3) {
      room {
        name
        capacity
      }
    }
  }
        '''

rcn_error = error_item
rcn_error.message = "Resource does not exist"
rcn_error.locations = [{"line": 3, "column": 6}]
rcn_error.path = ["roomsContainingResource"]
rcn_data = {"roomsContainingResource": None}
rooms_containing_non_existent_resource_expected_response = build(
    error=rcn_error.build_error(rcn_error),
    data=rcn_data
)
