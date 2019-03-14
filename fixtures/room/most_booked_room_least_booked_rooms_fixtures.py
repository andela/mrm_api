get_top_ten_rooms = '''
    {
        analyticsForMostBookedRooms(
            startDate:"Jul 11 2018", endDate:"Jul 11 2018")
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
          "meetings": 1,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

get_bottom_ten_rooms = '''
    {
        analyticsForLeastBookedRooms(
            startDate:"Jul 11 2018", endDate:"Jul 11 2018")
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
    "analyticsForLeastBookedRooms": {
      "analytics": [
        {
          "meetings": 1,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

test_for_division_error = '''
    {
        analyticsForLeastBookedRooms(
            startDate:"Jul 11 2018", endDate: "Jul 11 2018")
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''
