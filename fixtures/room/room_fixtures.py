room_mutation_query = '''
    mutation {
        createRoom(name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 1) {
            room {
                name
                roomType
                capacity
                floorId
            }
        }
    }
'''

room_mutation_response = {
    "data": {
        "createRoom": {
            "room": {
                "name": "Mbarara",
                "roomType": "Meeting",
                "capacity": 4,
                "floorId": 1,
            }
        }
    }
}

room_mutation_with_name_empty = '''
    mutation {
        createRoom(name: "", roomType: "Meeting", capacity: 4, floorId: 1) {
            room {
                name
                roomType
                capacity
                floorId
            }
        }
    }
'''

room_name_empty_response = {
    "errors": [
        {
            "message": "Room name is required field",
            "locations": [
                {
                "line": 2,
                "column": 3
                }
            ]
        }
    ],
    "data": {
        "createRoom": 'null'
    }
}

room_mutation_with_type_empty = '''
    mutation {
        createRoom(name: "Mbarara", roomType: "", capacity: 4, floorId: 1) {
            room {
                name
                roomType
                capacity
                floorId
            }
        }
    }
'''

room_type_empty_response = {
    "errors": [
        {
            "message": "Room room_type is required field",
            "locations": [
                {
                "line": 2,
                "column": 3
                }
            ]
        }
    ],
    "data": {
        "createRoom": 'null'
    }
}