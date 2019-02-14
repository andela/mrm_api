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
            'bookings': 64
        }, {
            'period': 'November',
            'bookings': 3
        }]
    }
}

get_bookings_count_monthly_diff_years = '''
query {
  bookingsAnalyticsCount(startDate:"Nov 1 2017", endDate:"May 1 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_monthly_diff_years_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'November',
            'bookings': 0
        }, {
            'period': 'December',
            'bookings': 0
        }, {
            'period': 'January',
            'bookings': 0
        }, {
            'period': 'February',
            'bookings': 0
        }, {
            'period': 'March',
            'bookings': 0
        }, {
            'period': 'April',
            'bookings': 0
        }, {
            'period': 'May',
            'bookings': 0
        }]
    }
}
