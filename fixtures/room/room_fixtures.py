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


rooms_query = '''
    {
    rooms{
                name
                capacity
                roomType
        }
    }
    '''
query_rooms_response = {
    "data": {
        "rooms": [
            {
        
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting"
            }
            ]
        }
    }

room_query_by_id = '''
                {
                getRoomById(roomId:1){
                    capacity
                    name
                    roomType
                }
                }
                '''

room_query_by_id_response = {
                    "data": {
                        "getRoomById": [
                        {
                            "capacity": 6,
                            "name": "Entebbe",
                            "roomType": "meeting"
                        }
                        ]
                    }
                    }