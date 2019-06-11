
query_get_rooms_in_location = '''{
getRoomsInALocation(locationId:1){
    name
    capacity
    roomType
    imageUrl
    }
}
'''

expected_query_get_rooms_in_location = {
"data": {
        "getRoomsInALocation": [
            {
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            },
            {
                "name": "Tana",
                "capacity": 14,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        ]
    }
}
