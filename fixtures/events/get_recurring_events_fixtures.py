recurring_event_query = '''
{
  allRecurringEvents(date: "feb 28 2019") {
    day
    events {
      startDate
      endDate
      roomName
      eventTitle
      recurringEventId
      eventId
    }
  }
}
'''

date_out_of_range_query = '''
{
  allRecurringEvents(date: "feb 30 2019") {
    day
    events {
      startDate
      endDate
      roomName
      eventTitle
      recurringEventId
      eventId
    }
  }
}
'''

wrong_date_format_query = '''
{
  allRecurringEvents(date: "21 jan 2019") {
    day
    events {
      startDate
      endDate
      roomName
      eventTitle
      recurringEventId
      eventId
    }
  }
}
'''
