
query_get_rooms_in_location = '''{
getRoomsInALocation(locationId:1){
    name
    abbreviation
    office {
          buildingName
        blocks {
            name
            floors {
                name
                rooms {
                    capacity
                    name
                    roomType
                }
            }
        }
        }
    }
}
'''

expected_query_get_rooms_in_location = {
"data": {
        "getRoomsInALocation": [
            {
                    "name": "Uganda",
                    "abbreviation": "KLA",
                    "office": [{
                        "buildingName": "EPIC Tower",
                        "blocks": [{
                            "name": "EC",
                            "floors": [{
                                "name": "3rd",
                                "rooms": [{
                                    "capacity": 6,  # noqa: E501
                                    "name": "Entebbe",  # noqa: E501
                                    "roomType": "meeting",  # noqa: E501
                                }]
                        }]
                    }]
                }]
            }
        ]
    }
}
