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
