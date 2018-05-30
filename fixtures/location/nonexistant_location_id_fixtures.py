

query_nonexistant_location_id = '''{
                                getRoomsInALocation(locationId:4){
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

expected_query_with_nonexistant_id = {
                            "data": {
                                "getRoomsInALocation": []
                            }
                            }
