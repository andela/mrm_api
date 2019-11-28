from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None
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

aaq_error = error_item
aaq_error.message = "Location Id does not exist"
aaq_error.locations = [{"line": 3, "column": 7}]
aaq_error.path = ["allAnalytics"]
aaq_data = {"allAnalytics": None}

all_analytics_query_response_super_admin_with_invalid_locationid = build(
    aaq_error.build_error(aaq_error),
    aaq_data
)
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
                    "events": [
                        {
                            "durationInMinutes": 890
                        }
                    ]
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
                    "events": [
                        {
                            "durationInMinutes": 155
                        }
                    ]
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
                    "events": [
                        {
                            "durationInMinutes": 92
                        }
                    ]
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
                    "events": [
                        {
                            "durationInMinutes": 0
                        }
                    ]
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
                    "events": [
                        {
                            "durationInMinutes": 0
                        }
                    ]
                }
            ],
            "bookingsCount": [
                {
                    "totalBookings": 7,
                    "period": "Jul 11 2018"
                },
                {
                    "totalBookings": 5,
                    "period": "Jul 12 2018"
                }
            ]
        }
    }
}
