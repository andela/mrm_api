null = None

query_update_all_fields = '''mutation{
    updateRoom(roomId: 1, name: "Jinja", capacity: 8, roomType: "board room"){ # noqa: E501
        room{
            name
            capacity
            roomType
        }
    }
}
'''

expected_query_update_all_fields = {
    "data": {
        "updateRoom": {
            "room": {
                "name": "Jinja",
                "capacity": 8,
                "roomType": "board room"
            }
        }
    }
}

query_update_only_required_field = '''mutation{
    updateRoom(roomId:1,name:"Jinja"){
        room {
            name
            capacity
            roomType
        }
    }
}
'''

expected_query_update_only_required_field = {
    "data": {
        "updateRoom": {
            "room": {
                "name": "Jinja",
                "capacity": 6,
                "roomType": "meeting"
            }
        }
    }
}

query_without_room_id = '''mutation{
            updateRoom(name:"Jinja"){
                room{
                    name
                    capacity
                    roomType
                    }
                }
                }
            '''

expected_query_without_room_id = {
    "errors": [
        {
            "message": "mutate() missing 1 required positional argument: 'room_id'",  # noqa: E501
            "locations": [{
                "line": 2,
                "column": 13
            }]
        }
    ],
    "data": {
        "updateRoom": null
    }
}


query_if_room_id_is_non_existant_room = '''mutation{
    updateRoom(roomId: 4, name: "Jinja", capacity: 8, roomType: "board room"){ # noqa: E501
        room{
            name
            capacity
            roomType
        }
    }
}
'''

expected_query_if_room_id_is_non_existant_room = {
    "errors": [
        {
            "message": "'NoneType' object has no attribute 'name'",  # noqa: E501
            "locations": [
                {
                    "line": 2,
                    "column": 5
                }
            ]
        }
    ],
    "data": {
        "updateRoom": null
    }
}


update_with_empty_field = '''mutation{
    updateRoom(roomId: 1, name:"", capacity:8, roomType: "board room"){
        room{
            name
            capacity
            roomType
        }
    }
}
'''

expected_response_update_with_empty_field = {
    "errors":  [
                    {
                        "message": "name is required field",
                        "locations": [
                            {
                                "line": 2,
                                "column": 5
                            }
                        ]
                    }
                ],
    "data": {
        "updateRoom": null
    }
}
