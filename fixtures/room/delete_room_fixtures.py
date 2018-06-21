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
