null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", 
            roomType: "Meeting", 
            capacity: 4, 
            floorId: 1, 
            calendarId:"andela.com_385@resource.calendar.google.com") {
            room {
                name
                roomType
                capacity
                floorId
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
                "floorId": 1,
            }
        }
    }
}


rooms_query = '''
    {
    rooms{
                name
                capacity
                roomType
                }
    }
    '''
query_rooms_response = {
    "data": {
        "rooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting"
            }]
    }
    }

room_query_by_id = '''
                {
                getRoomById(roomId:1){
                    capacity
                    name
                    roomType
                }
                }
                '''

room_query_by_id_response = {
                    "data": {
                        "getRoomById": [
                        {
                            "capacity": 6,
                            "name": "Entebbe",
                            "roomType": "meeting"
                        }
                        ]
                    }
                    }

room_with_non_existant_id = '''
                {
                getRoomById(roomId:7){
                    capacity
                    name
                    roomType
                }
                }
'''

room_query_with_non_existant_id_response = {
                                "errors": [
                                    {
                                    "message": "Room not found",
                                    "locations": [
                                        {
                                        "line": 3,
                                        "column": 17
                                        }
                                    ]
                                    }
                                ],
                                "data": {
                                    "getRoomById": null
                                }
                                }

room_schedule_query = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
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