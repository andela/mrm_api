null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, roomTags: [1], locationId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                id
                name
                roomType
                capacity
                locationId
                imageUrl
                roomTags {
                  name
                  description
                }
            }
        }
    }
'''

room_mutation_response = {
    "data": {
        "createRoom": {
            "room": {
                "name": "Mbarara",
                "roomType": "Meeting",
                "capacity": 4,
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        }
    }
}

room_invalid_location_id_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4,
            locationId: 9, roomTags: [1],
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
                roomTags {
                    name
                    color
                    description
                }
            }
        }
    }
'''

room_invalid_tag_mutation = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, roomTags: [8], locationId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                id
                name
                roomType
                capacity
                locationId
                imageUrl
            }
        }
    }
'''

room_name_empty_mutation = '''
    mutation {
        createRoom(
            name: "", roomType: "Meeting", capacity: 4,
            locationId: 1, roomTags: [1],
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
            }
        }
    }
'''

room_invalid_calendar_id_mutation_query = '''
    mutation {
        createRoom(
            name: "Kigali", roomType: "Meeting", capacity: 6, locationId: 1, roomTags: [1],
            calendarId:"andela.com_38363233383232303439@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
            }
        }
    }
'''

room_invalid_calendar_id_mutation_response = {
    "errors": [
        {
            "message": "Room calendar Id is invalid",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "createRoom"
            ]
        }
    ],
    "data": {
        "createRoom": null
    }
}

rooms_query = '''
query {
  allRooms{
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomTags {
          name
          color
      }
        }
    }
}
'''

db_rooms_query = '''
    {
    rooms{
                name
                capacity
                roomType
                imageUrl
                }
    }
    '''

db_rooms_query_response = {
    "data": {
        "rooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }]
    }
}

query_rooms_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "roomTags": [
                        {
                            "name": "Block-B",
                            "color": "green"
                        }
                    ],
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

room_mutation_query_duplicate_name = '''
    mutation {
        createRoom(
            name: "Entebbe", roomType: "Meeting", capacity: 4, roomTags: [1], locationId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                id
                name
                roomType
                capacity
                locationId
                imageUrl
                roomTags {
                  name
                  description
                }
            }
        }
    }
'''

room_mutation_query_duplicate_name_response = {
    "errors": [
        {
            "message": "Entebbe Room already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "createRoom"
            ]
        }
    ],
    "data": {
        "createRoom": null
    }
}

room_duplicate_calender_id_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, locationId:1,
            calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
            }
        }
    }
'''

room_duplicate_calendar_id_mutation_response = {
  "errors": [
    {
      "message": "andela.com_3630363835303531343031@resource.calendar.google.com CalenderId already exists",  # noqa: E501
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "createRoom"
      ]
    }
  ],
  "data": {
    "createRoom": null
  }
}
