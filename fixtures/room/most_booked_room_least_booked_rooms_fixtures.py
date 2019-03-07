get_top_ten_rooms = '''
    {
        analyticsForBookedRooms(
            startDate:"Jan 1 2019",
            endDate:"Jan 31 2019",
            limit:10,
            criteria:"most_booked")
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''

top_ten_response = {
  "data": {
    "analyticsForMostBookedRooms": {
      "analytics": [
        {
          "meetings": 2,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

get_bottom_ten_rooms = '''
    {
        analyticsForBookedRooms(
            startDate:"Jan 1 2019",
            endDate:"Jan 31 2019",
            limit:10,
            criteria:"least_booked")
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''

bottom_ten_response = {
  "data": {
    "analyticsForBookedRooms": {
      "analytics": [
        {
          "meetings": 2,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

top_ten_response = {
  "data": {
    "analyticsForBookedRooms": {
      "analytics": [
        {
          "meetings": 2,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

test_for_division_error = '''
    {
        analyticsForBookedRooms(
            startDate:"Aug 8 2018", endDate: "Aug 12 2018", limit:10)
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''
