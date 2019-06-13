filter_rooms_by_capacity = '''query {
  allRooms(capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_location = '''query {
  allRooms(location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_location_response = {
    "data": {
        "allRooms": {
            "rooms": [
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
}
filter_rooms_by_wings_and_floors = '''
    query {
    allRooms(roomLabels:"1st Floor, Wing A") {
        rooms {
        id
        name
        roomLabels
        }
    }
    }
    '''

filter_rooms_by_wings_and_floors_response = {
    'data': {
        'allRooms': {
            'rooms': [
                {
                    'id': '1',
                    'name': 'Entebbe',
                    'roomLabels': [
                        '1st Floor',
                        'Wing A'
                    ]
                }
            ]
        }
    }
}
filter_rooms_by_non_existent_room_label = '''
    query {
    allRooms(roomLabels:"Random") {
        rooms {
        id
        name
        roomLabels
        }
    }
    }
    '''

filter_rooms_by_non_existent_room_label_response = {
    'data': {
        'allRooms': {
            'rooms': []
        }
    }
}
filter_rooms_by_location_capacity = '''query {
  allRooms(location:"Kampala",capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_location_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_resources_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_tag = '''query {
    filterRoomsByTag(tagId: 1){
        id
        name
        }
    }'''

filter_rooms_by_tag_response = {
    "data": {
        "filterRoomsByTag": [
            {
                "id": "1",
                "name": "Entebbe"
            }
        ]
    }
}

filter_rooms_by_invalid_tag = '''query {
    filterRoomsByTag(tagId: 100){
        id
        name
        }
    }'''

filter_rooms_by_invalid_tag_error_response = {
    "errors": [
        {
            "message": "No rooms found with this tag",
            "locations": [
                {
                    "line": 2,
                    "column": 5
                }
            ],
            "path": [
                "filterRoomsByTag"
            ]
        }
    ],
    "data": {
        "filterRoomsByTag": None
    }
}

filter_rooms_by_room_labels = '''query {
  allRooms(roomLabels:"Wing A"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''

filter_rooms_by_room_labels_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",  # noqa: E501
                    "roomLabels": ["1st Floor", "Wing A"]
                }
            ]
        }
    }
}
filter_rooms_by_location_room_labels = '''query {
  allRooms(roomLabels:"Wing A", location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''
filter_rooms_by_resource = '''query {
  allRooms(resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''

filter_rooms_by_location_resource = '''query {
  allRooms(resources:"Markers", location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''
