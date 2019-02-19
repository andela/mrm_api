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

query_room_id_non_existant = '''mutation{
    updateRoom(roomId: 4, name: "Jinja", capacity: 8, roomType: "board room"){ # noqa: E501
        room{
            name
            capacity
            roomType
        }
    }
}
'''

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

response_for_update_room_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 2,
                    "column": 5
                }
                ],
            "path": [
                "updateRoom"
            ]
        }
    ],
    "data": {"updateRoom": null}}
