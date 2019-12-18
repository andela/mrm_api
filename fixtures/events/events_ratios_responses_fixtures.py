from ..output.OutputBuilder import build
from ..output.Error import error_item

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

event_ratio_percentage_cancellation_response = {
    "data": {
        "analyticsRatios": {
            "cancellationsPercentage": 33.33333333333333
        }
    }
}

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

ers_error = error_item
ers_error.message = "Room not found"
ers_error.locations = [{'line': 2, 'column': 5}]
ers_error.path = ['analyticsRatiosPerRoom']
ers_data = {'analyticsRatiosPerRoom': None}
event_ratio_single_room_with_non_existing_id_response = build(
    ers_error.build_error(ers_error),
    ers_data
)
