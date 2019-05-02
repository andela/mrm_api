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

rooms_containing_non_existent_resource_expected_response = {
  "errors": [
    {
      "message": "Resource does not exist",
      "locations": [
        {
          "line": 3,
          "column": 6
        }
      ],
      "path": [
        "roomsContainingResource"
      ]
    }
  ],
  "data": {
    "roomsContainingResource": None
  }
}
