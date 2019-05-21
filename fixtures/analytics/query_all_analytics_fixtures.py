null = None

all_analytics_query = '''
    query {
        allAnalytics(startDate:"jul 11 2018", endDate:"jul 12 2018") {
            bookings
            analytics{
                roomName
                cancellations
                autoCancellations
                numberOfMeetings
                checkins
                checkinsPercentage
                percentageShare
                appBookings
                appBookingsPercentage
                bookingsCount{
                    period
                    bookings
                }
                events{
                    durationInMinutes
                }
            }
        }
    }
'''

all_analytics_query_response = {
    "data": {
        "allAnalytics": {
            "bookings": 1,
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "cancellations": 0,
                    "autoCancellations": 0,
                    "numberOfMeetings": 1,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "percentageShare": 100.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "bookingsCount": [
                        {
                            "period": "Jul 11 2018",
                            "bookings": 1
                        }
                    ],
                    "events": [
                        {
                            "durationInMinutes": 45
                        }
                    ]
                },
            ]
        }
    }
}

analytics_query_for_date_ranges = '''
    query {
        allAnalytics(startDate:"jul 11 2019", endDate:"jul 12 2018") {
            bookings
            analytics{
                roomName
                cancellations
                autoCancellations
                numberOfMeetings
                checkins
                checkinsPercentage
                percentageShare
                appBookings
                appBookingsPercentage
                bookingsCount{
                    period
                    bookings
                }
                events{
                    durationInMinutes
                }
            }
        }
    }
'''
