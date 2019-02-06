get_top_ten_rooms = '''
    {
        analyticsForMostBookedRooms(
            startDate:"Jan 1 2019", endDate:"Jan 31 2019")
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''

get_bottom_ten_rooms = '''
    {
        analyticsForLeastBookedRooms(
            startDate:"Jan 1 2019", endDate:"Jan 31 2019")
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
          "meetings": 29,
          "percentage": 100,
          "roomName": "Entebbe",
        }
      ]
    }
  }
}

top_ten_response = {
  "data": {
    "analyticsForMostBookedRooms": {
      "analytics": [
        {
          "meetings": 29,
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
            startDate:"Aug 8 2018", endDate: "Aug 12 2018")
        {
            analytics {
                roomName
                meetings
                percentage
            }
        }
    }
'''
