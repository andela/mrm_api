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
        cancelledEvent(
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
        "cancelledEvent": {
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
