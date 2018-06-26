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
