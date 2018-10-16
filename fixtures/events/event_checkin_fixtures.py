event_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:
        "andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_data_1234"){
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
    'data': {
        'eventCheckin': {
            'event': {
                'cancelled': False,
                'checkedIn': True,
                'eventId': 'test_data_1234',
                'room': {
                    'calendarId': 'andela.com_3630363835303531343031@resource.calendar.google.com',  # noqa: E501
                    'id': '1',
                    'name': 'Entebbe'
                    },
                'roomId': 1
                }
            }
        }
    }

wrong_calendar_id_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"fake_calendar_id",
        eventId:"test_data_1234"){
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
