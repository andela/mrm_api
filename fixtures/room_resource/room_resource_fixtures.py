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

resource_mutation_empty_name = '''
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


<<<<<<< HEAD
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
=======
resource_mutation_0_room_id = '''
>>>>>>> [Bug 158140829] Fix flake8 errors
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
