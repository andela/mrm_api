null = None

delete_room_query = '''
                    mutation{
                    deleteRoom(roomId:1){
                    room{
                        name
                        capacity
                        roomType
                    }
                    }
                    }
                    '''

expected_response_room_query = {
                        "data": {
                            "deleteRoom": {
                                "room": {
                                    "name": "Entebbe",
                                    "capacity": 6,
                                    "roomType": "meeting"
                                    }
                                    }
                                    }
                                    }

delete_room_query_non_existant_room_id = '''
                    mutation{
                    deleteRoom(roomId:89){
                    room{
                        name
                        capacity
                        roomType
                    }
                    }
                    }
                    '''

expected_response_non_existant_room_id = {
                                            "errors": [
                                                {
                                                    "message": "RoomId not found",  # noqa: E501
                                                    "locations": [
                                                        {
                                                        "line": 3,
                                                        "column": 21
                                                        }
                                                        ]
                                                        }
                                                        ],
                                            "data": {
                                                "deleteRoom": null
                                                    }
                                                    }

response_for_delete_room_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 21
                }
                ],
            "path": [
                "deleteRoom"
            ]
        }
    ],
    "data": {"deleteRoom": null}}
