null = None

all_remote_rooms_query = '''
 query {
  allRemoteRooms {
    rooms {
      calendarId
      name
    }
  }
}
'''

paginated_rooms_query = '''
 query {
  allRooms(page:1, perPage:1){
   rooms{
      name
   }
   hasNext
   hasPrevious
   pages
}
}
'''

paginated_rooms_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe"
                }
            ],
            "hasNext": True,
            "hasPrevious": False,
            "pages": 2
        }
    }
}

room_query_by_id = '''
{
    getRoomById(roomId: 1){
        capacity
        name
        roomType
    }
}
'''

room_query_by_id_response = {
    "data": {
        "getRoomById": {
            "capacity": 6,
            "name": "Entebbe",
            "roomType": "meeting"
        }
    }
}

room_with_non_existant_id = '''{
    getRoomById(roomId: 100) {
        id
        name
    }
}
'''

room_query_with_non_existant_id_response = "Room not found"

room_occupants_query = '''
                        {
                        roomOccupants(
                            calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
                            days:7){
                        occupants
                        }
                        }
                        '''

room_occupants_query_response = {
    "data": {
        "roomOccupants":
            {"occupants": "['philip.wafula@andela.com', 'joy.uzosike@andela.com']"  # noqa: E501
        }
    }
}

room_schedule_query = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
                            days:7){
                        events
                        }
                        }
                        '''

room_schedule_query_response = {
    "data": {
        "roomSchedule":
            {"events": "[{'start': '2019-01-22T05:30:00-08:00', 'summary': 'SD sync'}, {'start': '2019-01-22T06:00:00-08:00', 'summary': 'Uzo<>Philip'}]"}  # noqa: E501
    }
}

room_schedule_query_with_non_existant_calendar_id = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_38363230343935@resource.calendar.google.com",
                            days:7){
                        events
                        }
                        }
                        '''
room_occupants_query_with_non_existant_calendar_id = '''
                        {
                        roomOccupants(
                            calendarId:"andela.com_38363230343935@resource.calendar.google.com",
                            days:7){
                        occupants
                        }
                        }
                        '''

room_occupants_of_non_existant_calendar_id_response = {
    "errors": [
        {
            "message": "Invalid CalendarId",
            "locations": [
                {
                    "line": 1,
                    "column": 2
                }
            ]
        }
    ],
    "data": {
        "roomSchedule": null
    }
}
room_schedule_of_non_existant_calendar_id_response = {
    "errors": [
        {
            "message": "Invalid CalendarId",
            "locations": [
                {
                    "line": 1,
                    "column": 2
                }
            ]
        }
    ],
    "data": {
        "roomSchedule": null
    }
}

room_search_by_name = '''
{
    getRoomByName(name:"Entebbe"){
        name
    }
}
'''
room_search_by_name_response = {
    "data": {
        "getRoomByName": [
            {
                "name": "Entebbe"
            }]
    }
}

room_search_by_empty_name = '''
{
    getRoomByName(name:""){
        name
        }
}

'''
room_search_by_empty_name_response = "Please input Room Name"

room_search_by_invalid_name = '''
{
    getRoomByName(name:"bbbb"){
        name
    }
}
'''

room_search_by_invalid_name_response = "Room not found"

paginated_rooms_query_blank_page = '''
 query {
  allRooms(page:6, perPage:1){
   rooms{
      name
   }
   hasNext
   hasPrevious
   pages
}
}
'''

room_occupants_invalid_calendar_id_query = '''
    {
    roomOccupants(
        calendarId:"abcd",
        days:7){
    occupants
    }
    }
    '''
