sync_data_mutation = """
mutation{
    syncEventData{
        message
        }
    }
"""

notification_mutation = """
mutation{
    mrmNotification(calendarId: \
    "andela.com_3630363835303531343031@resource.calendar.google.com"){
        message
        }
    }
"""
