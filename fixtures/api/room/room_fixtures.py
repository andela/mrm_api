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
