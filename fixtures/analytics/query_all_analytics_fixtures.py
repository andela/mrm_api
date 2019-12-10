all_analytics_query = """
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
          deviceAnalytics{
            deviceName
            deviceId
          }
        }
  }
"""
all_analytics_query_down_time = """
    query {
        allAnalytics(startDate:"jul 11 2018", endDate:"jul 12 2018", locationId:1) { # noqa: E501
        deviceAnalytics{
            downTime
          }
        }
  }
"""
all_analytics_query_invalid_locationid = """
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
"""

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
                    "events": [{"durationInMinutes": 45}],
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
                    "events": [{"durationInMinutes": 0}],
                },
            ],
            "bookingsCount": [
                {"totalBookings": 1, "period": "Jul 11 2018"},
                {"totalBookings": 0, "period": "Jul 12 2018"},
            ],
            "deviceAnalytics": [
                {
                    "deviceName": "Samsung",
                    "deviceId": 1,
                    # "downTime": "this device was seen {}".format(
                    #     downtime_value),
                }
            ],
        }
    }
}

all_analytics_query_response_super_admin_with_invalid_locationid = {
    "errors": [
        {
            "message": "Location Id does not exist",
            "locations": [{"line": 3, "column": 7}],
            "path": ["allAnalytics"],
        }
    ],
    "data": {"allAnalytics": None},
}

all_analytics_query_response_super_admin = {
    "data": {
        "allAnalytics": {
            "checkinsPercentage": 0.0,
            "appBookingsPercentage": 0.0,
            "autoCancellationsPercentage": 0.0,
            "cancellationsPercentage": 0.0,
            "bookings": 12,
            "analytics": [
                {
                    "roomName": "Oculus",
                    "cancellations": 0,
                    "cancellationsPercentage": 0.0,
                    "autoCancellations": 0,
                    "numberOfBookings": 6,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "bookingsPercentageShare": 50.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "events": [{"durationInMinutes": 890}],
                },
                {
                    "roomName": "Krypton",
                    "cancellations": 0,
                    "cancellationsPercentage": 0.0,
                    "autoCancellations": 0,
                    "numberOfBookings": 3,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "bookingsPercentageShare": 25.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "events": [{"durationInMinutes": 155}],
                },
                {
                    "roomName": "Bujumbura",
                    "cancellations": 0,
                    "cancellationsPercentage": 0.0,
                    "autoCancellations": 0,
                    "numberOfBookings": 3,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "bookingsPercentageShare": 25.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "events": [{"durationInMinutes": 92}],
                },
                {
                    "roomName": "Kampala",
                    "cancellations": 0,
                    "cancellationsPercentage": 0.0,
                    "autoCancellations": 0,
                    "numberOfBookings": 0,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "bookingsPercentageShare": 0.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "events": [{"durationInMinutes": 0}],
                },
                {
                    "roomName": "Algiers",
                    "cancellations": 0,
                    "cancellationsPercentage": 0.0,
                    "autoCancellations": 0,
                    "numberOfBookings": 0,
                    "checkins": 0,
                    "checkinsPercentage": 0.0,
                    "bookingsPercentageShare": 0.0,
                    "appBookings": 0,
                    "appBookingsPercentage": 0.0,
                    "events": [{"durationInMinutes": 0}],
                },
            ],
            "bookingsCount": [
                {"totalBookings": 7, "period": "Jul 11 2018"},
                {"totalBookings": 5, "period": "Jul 12 2018"},
            ],
        }
    }
}

analytics_query_for_date_ranges = """
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
"""
