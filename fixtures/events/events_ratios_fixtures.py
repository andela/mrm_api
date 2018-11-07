event_ratio_query = '''query {
    analyticsRatios(startDate:"Jul 10 2018", endDate:"Jul 29 2018"){
    Bookings
    Checkins
}
}
'''

event_ratio_response = {
    "data": {
        "analyticsRatios": {
            "Bookings": 0,
            "Checkins": 0
        }
    }
}

event_ratio_for_one_day_query = '''query {
    analyticsRatios(startDate:"Jul 10 2018"){
    Bookings
    Checkins
}
}
'''
