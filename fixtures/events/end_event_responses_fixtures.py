end_event_mutation_response = {
  "data": {
    "endEvent": {
      "event": {
        "eventId": "test_id5",
        "eventTitle": "Onboarding",
        "checkedIn": True,
        "cancelled": False,
        "meetingEndTime": "2018-07-10T09:45:00Z",
        "room": {
          "id": "1",
          "name": "Entebbe",
          "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa: E501
        }
      }
    }
  }
}

end_unchecked_in_event_mutation_response = "Event yet to be checked in"

end_event_twice_mutation_response = "Event has already ended"
