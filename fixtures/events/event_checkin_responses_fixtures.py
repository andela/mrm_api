from ..output.OutputBuilder import build

event_checkin_data = {
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

event_checkin_response = build(
    data=event_checkin_data
)

cancel_event_respone = "Event cancelled but email not sent"

response_for_event_existing_in_db_checkin = build(
    data=event_checkin_data
)
