
query_get_rooms_in_location = '''{
                                getRoomsInALocation(locationId:1){
                                    name
                                    abbreviation
                                    block{
                                        name
                                        floor{
                                                name
                                                room{
                                                    capacity
                                                    name
                                                    roomType
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
                                                "block": [{
                                                        "name": "EC",
                                                        "floor": [{
                                                                "name": "3rd",
                                                                "room": [{
                                                                    "capacity":6,
                                                                    "name":"Entebbe",
                                                                    "roomType":"meeting",
                                                                }]
                                                        }]
                                                }]
                                            }
                                            ]
                                        }
                                        }
