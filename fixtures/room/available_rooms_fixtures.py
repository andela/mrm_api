
available_rooms_query = '''
query {
  allAvailableRooms(
              startDate: "Nov 07 2018",
              startTime: "08:00:00",
              endDate: "Nov 11 2018",
              endTime: "09:45:00",
              timeZone: "Africa/Kampala"
  ){
   availableRoom{
      id
      name
    }
    }
}
'''

available_rooms_query_with_empty_input = '''
query {
  allAvailableRooms(
              startDate: "",
              startTime: "08:00:00",
              endDate: "Nov 11 2018",
              endTime: "09:45:00",
              timeZone: "Africa/Kampala"
  ){
   availableRoom{
      name
    }
    }
}
'''

available_rooms_query_when_startDate_is_bigger_than_endDate = '''
query {
  allAvailableRooms(
              startDate: "Nov 13 2018",
              startTime: "08:00:00",
              endDate: "Nov 11 2018",
              endTime: "09:45:00",
              timeZone: "Africa/Kampala"
  ){
   availableRoom{
      name
    }
    }
}
'''

available_rooms_query_when_startTime_is_bigger_than_endTime = '''
query {
  allAvailableRooms(
              startDate: "Nov 07 2018",
              startTime: "10:00:00",
              endDate: "Nov 11 2018",
              endTime: "09:45:00",
              timeZone: "Africa/Kampala"
  ){
   availableRoom{
      name
    }
    }
}
'''
