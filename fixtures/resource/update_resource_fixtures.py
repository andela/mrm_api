
null = None

update_room_resource_query = '''
                        mutation{
                        updateRoomResource(roomId:1,resourceId:1,name:"TV Screen"){
                            resource{
                            name
                            }
                        }
                        }
                        '''

expected_update_room_resource_query = {
                        "data": {
                            "updateRoomResource": {
                            "resource": {
                                "name": "TV Screen"
                            }
                            }
                        }
                        }

non_existant_room_id_query = '''
                        mutation{
                        updateRoomResource(roomId:6,resourceId:1,name:"TV Screen"){
                            resource{
                            name
                            }
                        }
                        }
                        '''

expected_non_existant_room_id_query = {
                        "errors": [
                            {
                            "message": "RoomId not found",
                            "locations": [
                                {
                                "line": 3,
                                "column": 25
                                }
                            ]
                            }
                        ],
                        "data": {
                            "updateRoomResource": null
                        }
                        }

non_existant_resource_id_query = '''
                        mutation{
                        updateRoomResource(roomId:1,resourceId:6,name:"TV Screen"){
                            resource{
                            name
                            }
                        }
                        }
                        '''

expected_non_existant_resource_id_query= {
                        "errors": [
                            {
                            "message": "ResourceId not found",
                            "locations": [
                                {
                                "line": 3,
                                "column": 25
                                }
                            ]
                            }
                        ],
                        "data": {
                            "updateRoomResource": null
                        }
                        }
