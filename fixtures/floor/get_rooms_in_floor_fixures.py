get_rooms_in_floor = '''
{
    getRoomsInAFloor(floorId: 1) {
        name
        rooms {
            id
            name
            floorId
        }
    }
}
'''

get_rooms_in_floor_response = {
  "data": {
        "getRoomsInAFloor": [
            {
                "name": "3rd",
                "rooms": [
                    {
                        "id": "1",
                        "name": "Entebbe",
                        "floorId": 1
                    }
                ]
            }
        ]
    }
}