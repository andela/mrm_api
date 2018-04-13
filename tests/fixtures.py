room_mutation_query = '''
    mutation {
        createRoom(name: "Mbarara", type: "Meeting", capacity: 4, floorId: 1) {
            room {
                name
                type
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
                "type": "Meeting",
                "capacity": 4,
                "floorId": 1,
            }
        }
    }
}
