null = None

get_bookings_count_daily = '''
query {
  bookingsAnalyticsCount(startDate:"Nov 10 2018", endDate:"Nov 14 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_daily_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'Nov 10 2018',
            'bookings': 0
        }, {
            'period': 'Nov 11 2018',
            'bookings': 0
        }, {
            'period': 'Nov 12 2018',
            'bookings': 2
        }, {
            'period': 'Nov 13 2018',
            'bookings': 1
        }, {
            'period': 'Nov 14 2018',
            'bookings': 3
        }]
    }
}

get_bookings_count_monthly = '''
query {
  bookingsAnalyticsCount(startDate:"Aug 1 2018", endDate:"Nov 1 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_monthly_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'August',
            'bookings': 0
        }, {
            'period': 'September',
            'bookings': 38
        }, {
            'period': 'October',
            'bookings': 65
        }, {
            'period': 'November',
            'bookings': 3
        }]
    }
}

get_bookings_count_invalid_date_range = '''
query {
  bookingsAnalyticsCount(startDate:"Aug 1 2018", endDate:"Aug 30 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_invalid_date_range_response = {
    "errors": [{
        "message":
        "Kindly enter a valid date range(less than 15 days or greater than 90 days",  # noqa E501
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": ["bookingsAnalyticsCount"]
    }],
    "data": {
        "bookingsAnalyticsCount": null
    }
}
