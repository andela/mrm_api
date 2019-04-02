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

get_single_room_daily_count = '''
query {
  bookingsAnalyticsCount(
      startDate:"Jul 11 2018", endDate:"Jul 12 2018" roomId:1){
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
        "period": "Jul 11 2018",
        "bookings": 1
      },
      {
        "roomName": "Entebbe",
        "period": "Jul 12 2018",
        "bookings": 0
      }
    ]
  }
}

non_existing_room_id_query = '''
query {
  bookingsAnalyticsCount(
      startDate:"Jul 11 2018", endDate:"Jul 12 2018" roomId:100){
    roomName
   period
   bookings
  }
}
'''

non_existing_room_id_response = {
  "errors": [
    {
      "message": "Room Id does not exist",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "bookingsAnalyticsCount"
      ]
    }
  ],
  "data": {
    "bookingsAnalyticsCount": null
  }
}
