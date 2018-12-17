get_rooms_in_floor = '''
{
    getRoomsInAFloor(floorId: 4) {
        id
        name
        floorId
    }
}
'''

get_rooms_in_floor_response = {
  "data": {
        "getRoomsInAFloor": [
            {
                "id": "1",
                "name": "Entebbe",
                "floorId": 4
            }
        ]
    }
}
