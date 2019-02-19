null = None
event_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding",
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

event_checkin_response = {
    "data": {
        "eventCheckin": {
            "event": {
                "eventId": "test_id5",
                "roomId": 1,
                "checkedIn": True,
                "cancelled": False,
                "room": {
                    "id": "1",
                    "name": "Entebbe",
                    "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa
                }
            }
        }
    }
}

wrong_calendar_id_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"fake_calendar_id",
        eventId:"test_id5", eventTitle:"Onboarding",
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

cancel_event_mutation = '''
    mutation {
        cancelEvent(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding",
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z")
        {
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

cancel_event_respone = {
    "data": {
        "cancelEvent": {
            "event": {
                "eventId": "test_id5",
                "roomId": 1,
                "checkedIn": False,
                "cancelled": True,
                "room": {
                    "id": "1",
                    "name": "Entebbe",
                    "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa: E501
                }
            }
        }
    }
}

checkin_mutation_for_event_existing_in_db = '''mutation {
    eventCheckin(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding",
        startTime:"2018-07-11T09:00:00Z",
        endTime:"2018-07-11T09:45:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

response_for_event_existing_in_db_checkin = {
    "data": {
        "eventCheckin": {
            "event": {
                "eventId": "test_id5",
                "roomId": 1,
                "checkedIn": True,
                "cancelled": False,
                "room": {
                    "id": "1",
                    "name": "Entebbe",
                    "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa
                }
            }
        }
    }
}

response_for_wrong_migration = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 2,
                    "column": 5
                }
                ],
            "path": [
                "eventCheckin"
            ]
        }
    ],
    "data": {"eventCheckin": null}}
