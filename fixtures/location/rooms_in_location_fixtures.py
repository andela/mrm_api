
query_get_rooms_in_location = '''{
                                getRoomsInALocation(id:1){
                                    name
                                    abbreviation
                                    block{
                                    edges{
                                        node{
                                        name
                                        floor{
                                            edges{
                                            node{
                                                name
                                                room{
                                                edges{
                                                    node{
                                                    capacity
                                                    name
                                                    roomType
                                                    }
                                                }
                                            }
                                            }
                                        }
                                        }
                                    }
                                    }
                                }
                                }
                                }
                                        '''

expected_query_get_rooms_in_location ={
                                        "data": {
                                            "getRoomsInALocation": [
                                            {
                                                "name": "Uganda",
                                                "abbreviation": "KLA",
                                                "block": {
                                                "edges": [
                                                    {
                                                    "node": {
                                                        "name": "EC",
                                                        "floor": {
                                                        "edges": [
                                                            {
                                                            "node": {
                                                                "name": "3rd",
                                                                "room": {
                                                                "edges": [
                                                                    {
                                                                    "node":{
                                                                    "capacity":6,
                                                                    "name":"Entebbe",
                                                                    "roomType":"meeting",
                                                                    }
                                                                }
                                                                ]
                                                                }
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
