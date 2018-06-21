resource_mutation_query = '''
    mutation {
        createResource(name: "Speakers", roomId: 1, quantity: 3) {
            resource{
                name
                roomId
                quantity
            }
        }
    }
'''

resource_mutation_response = {
    "data": {
        "createResource": {
            "resource": {
                "name": "Speakers",
                "roomId": 1,
                "quantity": 3
            }
        }
    }
}

resource_mutation_empty_name_string_query = '''
    mutation {
        createResource(name: "", roomId: 1, quantity: 3) {
            resource{
                name
                roomId
                quantity
            }
        }
    }
'''

resource_mutation_quantity_string_query = '''
    mutation {
        createResource(name: "Makers", roomId: 1, quantity: 0) {
            resource{
                name
                roomId
                quantity
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

error_empty_name_string = {
  "errors": [
    {
      "locations": [
        {
          "column": 47,
          "line": 2
        }
      ],
      "message": "Argument \"quantity\" has invalid value \"4\".\nExpected type \"Int\", found \"4\"."
    }
  ]
}

error_quantity_string = {
  "errors": [
    {
      "message": "quantity is required field",
      "locations": [
        {
          "column": 9,
          "line": 3
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
            quantity: 3
            ) {
                resource{
                    name
                    roomId
                    quantity
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
