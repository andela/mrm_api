
rooms_in_block_query= '''
                    {
                    getRoomsInABlock(id:1){
                        name
                        floor{
                        edges{
                            node{
                            name
                            room{
                                edges{
                                node{
                                    name
                                    capacity
                                    roomType
                                }
                                }
                                
                            }
                            }
                        }
                        }
                        
                    }
                    }'''


rooms_in_block_query_response = {
                "data": {
                    "getRoomsInABlock": [
                    {
                        "name": "EC",
                        "floor": {
                        "edges": [
                            {
                            "node": {
                                "name": "3rd",
                                "room": {
                                "edges": [
                                    {
                                    "node": {
                                        "name": "Entebbe",
                                        "capacity": 6,
                                        "roomType": "meeting"
                                    }
                                    }
                                ]
                                }
                            }
                            }
                        ]
                        }
                    }
                    ]
                }
                }