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
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
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
                            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
                            days:7){
                        occupants
                        }
                        }
                        '''
room_schedule_query = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
                            days:7){
                        events
                        }
                        }
                        '''

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
