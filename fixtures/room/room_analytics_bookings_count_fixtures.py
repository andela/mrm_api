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
            'bookings': 2
        }, {
            'period': 'Nov 11 2018',
            'bookings': 2
        }, {
            'period': 'Nov 12 2018',
            'bookings': 2
        }, {
            'period': 'Nov 13 2018',
            'bookings': 2
        }, {
            'period': 'Nov 14 2018',
            'bookings': 2
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
            'bookings': 2
        }, {
            'period': 'September',
            'bookings': 2
        }, {
            'period': 'October',
            'bookings': 2
        }, {
            'period': 'November',
            'bookings': 2
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
            'bookings': 2
        }, {
            'period': 'December',
            'bookings': 2
        }, {
            'period': 'January',
            'bookings': 2
        }, {
            'period': 'February',
            'bookings': 2
        }, {
            'period': 'March',
            'bookings': 2
        }, {
            'period': 'April',
            'bookings': 2
        }, {
            'period': 'May',
            'bookings': 2
        }]
    }
}

get_single_room_daily_count = '''
query {
  bookingsAnalyticsCount(startDate:"Nov 10 2018",
   endDate:"Nov 12 2018", roomId:1){
   roomName
   period
   bookings
  }
}
'''

get_single_room_daily_count_response = {
  "data": {
    "bookingsAnalyticsCount": [
      {
        "roomName": "Entebbe",
        "period": "Nov 10 2018",
        "bookings": 2
      },
      {
        "roomName": "Entebbe",
        "period": "Nov 11 2018",
        "bookings": 2
      },
      {
        "roomName": "Entebbe",
        "period": "Nov 12 2018",
        "bookings": 2
      }
    ]
  }
}

non_existing_room_id_query = '''
query {
  bookingsAnalyticsCount(startDate:"Nov 10 2018",
   endDate:"Nov 12 2018", roomId:100){
   roomName
   period
   bookings
  }
}
'''
