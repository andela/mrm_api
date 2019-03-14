sync_data_mutation = """
mutation{
    syncEventData{
        message
        }
    }
"""

sync_data_response = {
  "data": {
    "syncEventData": {
      "message": "success"
    }
  }
}

notification_mutation = """
mutation{
    mrmNotification(calendarId: \
    "andela.com_3630363835303531343031@resource.calendar.google.com"){
        message
        }
    }
"""

notification_response = {
  "data": {
    "mrmNotification": {
      "message": "success"
    }
  }
}
