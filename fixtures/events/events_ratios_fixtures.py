event_ratio_query = '''query {
    analyticsRatios(startDate:"Jul 10 2018", endDate:"Jul 29 2018"){
        bookings
        checkins
        cancellations
        cancellationsPercentage
        checkinsPercentage
        appBookings
        appBookingsPercentage
}
}
'''

event_ratio_response = {
    "data": {
        "analyticsRatios": {
            "bookings": 1,
            "checkins": 0,
            "cancellations": 0,
            "cancellationsPercentage": 0,
            "checkinsPercentage": 0,
            'appBookings': 0,
            'appBookingsPercentage': 0
        }
    }
}

event_ratio_for_one_day_query = '''query {
    analyticsRatios(startDate:"Jul 11 2018"){
        bookings
        checkins
        cancellations
        cancellationsPercentage
        checkinsPercentage
        appBookings
        appBookingsPercentage
    }
}'''

event_ratio_per_room_query = '''query{
    analyticsRatiosPerRoom(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
        ratios{
            roomName
            bookings
            checkins
            checkinsPercentage
            cancellations
            cancellationsPercentage
            appBookings
            appBookingsPercentage
        }
    }
}'''

event_ratio_per_room_response = {
    'data': {
        'analyticsRatiosPerRoom': {
            'ratios': [
                {
                    'roomName': 'Entebbe',
                    'bookings': 1,
                    'checkins': 0,
                    'checkinsPercentage': 0,
                    'cancellations': 0,
                    'cancellationsPercentage': 0,
                    'appBookings': 0,
                    'appBookingsPercentage': 0
                }
            ]
        }
    }
}

event_ratio_percentage_cancellation_query = '''query {
    analyticsRatios(startDate:"Jul 10 2018", endDate:"Jul 29 2018"){
        cancellationsPercentage
}
}
'''

event_ratio_percentage_cancellation_response = {
    "data": {
        "analyticsRatios": {
            "cancellationsPercentage": 33.33333333333333
        }
    }
}

event_ratio_single_room_query = '''query{
    analyticsRatiosPerRoom(startDate:"Mar 1 2019", endDate:"Mar 27 2019",
    roomId:1){
        ratio{
            roomName
            bookings
            checkins
            checkinsPercentage
            cancellations
            cancellationsPercentage
            appBookings
            appBookingsPercentage
        }
    }
}'''

event_ratio_single_room_response = {
    "data": {
        "analyticsRatiosPerRoom": {
            "ratio": {
                "roomName": "Entebbe",
                "bookings": 0,
                "checkins": 0,
                "checkinsPercentage": 0.0,
                "cancellations": 0,
                "cancellationsPercentage": 0.0,
                "appBookings": 0,
                "appBookingsPercentage": 0.0
            }
        }
    }
}

event_ratio_single_room_query_with_non_existing_id = '''query{
    analyticsRatiosPerRoom(startDate:"Mar 1 2019", endDate:"Mar 27 2019",
    roomId:5){
        ratio{
            roomName
            bookings
            checkins
            checkinsPercentage
            cancellations
            cancellationsPercentage
            appBookings
            appBookingsPercentage
        }
    }
}'''

event_ratio_single_room_with_non_existing_id_response = {
    "errors": [
        {
            "message": "Room not found",
            "locations": [
                {
                    "line": 2,
                    "column": 5
                }
            ],
            "path": [
                "analyticsRatiosPerRoom"
            ]
        }
    ],
    "data": {
        "analyticsRatiosPerRoom": None
    }
}
