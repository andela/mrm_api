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

event_ratio_percentage_cancellation_query = '''query {
    analyticsRatios(startDate:"Jul 10 2018", endDate:"Jul 29 2018"){
        cancellationsPercentage
}
}
'''

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
