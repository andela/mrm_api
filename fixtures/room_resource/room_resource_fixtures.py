null = None
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


resource_mutation_0_room_id = '''
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

response_for_create_room_resource_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 5
                }
                ],
            "path": [
                "createRoomResource"
            ]
        }
    ],
    "data": {"createRoomResource": null}}
