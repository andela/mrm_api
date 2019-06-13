all_analytics_query = '''
    query {
      allAnalytics(startDate:"jul 11 2018", endDate:"jul 12 2018") {
          checkinsPercentage
          appBookingsPercentage
          autoCancellationsPercentage
          cancellationsPercentage
          bookings
          analytics{
            roomName
            cancellations
            cancellationsPercentage
            autoCancellations
            numberOfBookings
            checkins
            checkinsPercentage
            bookingsPercentageShare
            appBookings
            appBookingsPercentage
            events{
              durationInMinutes
              }
          }
          bookingsCount{
            totalBookings
            period
          }
        }
  }
'''

all_analytics_query_response = {
  "data": {
    "allAnalytics": {
      "checkinsPercentage": 0.0,
      "appBookingsPercentage": 0.0,
      "autoCancellationsPercentage": 0.0,
      "cancellationsPercentage": 0.0,
      "bookings": 1,
      "analytics": [
        {
          "roomName": "Entebbe",
          "cancellations": 0,
          "cancellationsPercentage": 0.0,
          "autoCancellations": 0,
          "numberOfBookings": 1,
          "checkins": 0,
          "checkinsPercentage": 0.0,
          "bookingsPercentageShare": 100.0,
          "appBookings": 0,
          "appBookingsPercentage": 0.0,
          "events": [
            {
              "durationInMinutes": 45
            }
          ]
        },
        {
          "roomName": "Tana",
          "cancellations": 0,
          "cancellationsPercentage": 0.0,
          "autoCancellations": 0,
          "numberOfBookings": 0,
          "checkins": 0,
          "checkinsPercentage": 0.0,
          "bookingsPercentageShare": 0.0,
          "appBookings": 0,
          "appBookingsPercentage": 0.0,
          "events": [
            {
              "durationInMinutes": 0
            }
          ]
        }
      ],
      "bookingsCount": [
        {
          "totalBookings": 1,
          "period": "Jul 11 2018"
        },
        {
          'totalBookings': 0,
          'period': 'Jul 12 2018'
        }
      ]
    }
  }
}
analytics_query_for_date_ranges = '''
    query {
      allAnalytics(startDate:"jul 11 2020", endDate:"jul 12 2018") {
          checkinsPercentage
          appBookingsPercentage
          autoCancellationsPercentage
          cancellationsPercentage
          bookings
          analytics{
            roomName
            cancellations
            cancellationsPercentage
            autoCancellations
            numberOfBookings
            checkins
            checkinsPercentage
            bookingsPercentageShare
            appBookings
            appBookingsPercentage
            events{
              durationInMinutes
              }
          }
          bookingsCount{
            totalBookings
            period
          }
        }
  }
'''
