from ..output.OutputBuilder import build
from ..output.Error import error_item

daily_room_events_response = {
    "data": {
        "analyticsForDailyRoomEvents": {
            "DailyRoomEvents": [
                {
                    "day": "Wed Jul 11 2018",
                    "events": [
                        {
                            'endTime': '09:45:00',
                            'eventSummary': 'Onboarding',
                            'noOfParticipants': 4,
                            'roomName': 'Entebbe',
                            'startTime': '09:00:00'
                        }
                    ]
                }
            ]
        }
    }
}

daily_paginated_room_events_response = {
    "data": {
        "analyticsForDailyRoomEvents": {
            "DailyRoomEvents": [
                {
                    "day": "Wed Jul 11 2018",
                    "events": [
                        {
                            "eventSummary": "Onboarding",
                            "startTime": "09:00:00",
                            "endTime": "09:45:00",
                            "roomName": "Entebbe",
                            "noOfParticipants": 4
                        }
                    ]
                }
            ],
            "pages": 1,
            "hasNext": False,
            "hasPrevious": False
        }
    }
}

dew_error = error_item
dew_error.message = "time data '10 jan 2019' does not match format '%b %d %Y'"
dew_error.locations = [{'line': 3, 'column': 5}]
dew_error.path = ['analyticsForDailyRoomEvents']
dew_data = {'analyticsForDailyRoomEvents': None}
daily_events_wrong_date_format_response = build(
    dew_error.build_error(dew_error),
    dew_data
)
