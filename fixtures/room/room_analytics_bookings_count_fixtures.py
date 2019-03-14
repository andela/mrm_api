null = None

get_bookings_count_daily = '''
query {
  bookingsAnalyticsCount(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_daily_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'Jul 11 2018',
            'bookings': 1
        }]
    }
}

get_bookings_count_monthly = '''
query {
  bookingsAnalyticsCount(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_monthly_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'Jul 11 2018',
            'bookings': 1
        }]
    }
}

get_bookings_count_monthly_diff_years = '''
query {
  bookingsAnalyticsCount(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
   period
   bookings
  }
}
'''

get_bookings_count_monthly_diff_years_response = {
    'data': {
        'bookingsAnalyticsCount': [{
            'period': 'Jul 11 2018',
            'bookings': 1
        }]
    }
}
