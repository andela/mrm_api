null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 1,
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                floorId
                imageUrl
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
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        }
    }
}


rooms_query = '''
    {
    allRooms{
                name
                capacity
                roomType
                imageUrl
                }
    }
    '''
query_rooms_response = {
    "data": {
        "allRooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }]
    }
}

room_query_by_id = '''
{
    getRoomById(roomId: 1){
        capacity
        name
        roomType
    }
}
'''

room_query_by_id_response = {
    "data": {
        "getRoomById": {
            "capacity": 6,
            "name": "Entebbe",
            "roomType": "meeting"
        }
    }
}

room_query_by_nonexistant_id = '''{
    getRoomById(roomId: 100) {
        id
        name
    }
}
'''

room_query_by_nonexistant_id_response = {
    "errors": [{
        "message": "Room not found",
        "locations": [{
                "line": 2,
                "column": 5
            }
        ]
    }],
    "data": {
        "getRoomById": null
    }
}
