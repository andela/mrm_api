resource_mutation_query = '''
    mutation {
        createResource(name: "Speakers", roomId: 1) {
            resource{
                name
                roomId
            }
        }
    }
'''

resource_mutation_response = {
    "data": {
        "createResource": {
            "resource": {
                "name": "Speakers",
                "roomId": 1
            }
        }
    }
}

resource_mutation_empty_name_string_query = '''
    mutation {
        createResource(name: "", roomId: 1) {
            resource{
                name
                roomId
            }
        }
    }
'''

error_empty_name_string = {
  "errors": [
    {
      "message": "name is required field",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ]
    }
  ],
  "data": {
    "createResource": None
  }
}

resource_mutation_0_value_room_id_query = '''
    mutation {
        createResource(
            name: "Speaker"
            roomId: 0
            ) {
                resource{
                    name
                    roomId
                    id
                }
            }
    }
'''

error_0_value_room_id = {
  "errors": [
    {
      "message": "room_id is required field",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ]
    }
  ],
  "data": {
    "createResource": None
  }
}
