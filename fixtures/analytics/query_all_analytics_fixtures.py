all_analytics_query = '''
    query {
      allAnalytics(startDate:"jul 11 2018", endDate:"jul 12 2018", locationId:1) { # noqa: E501
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
all_analytics_query_invalid_locationid = '''
    query {
      allAnalytics(startDate:"jul 11 2018", endDate:"jul 12 2018", locationId:10) { # noqa: E501
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
