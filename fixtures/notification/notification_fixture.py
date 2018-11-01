null = None
true = True
false = False

# when run for the first time for a user not already in the notifications table,
# the user is automatically added and the field is populated with the
# default value (True).
user_notification_query = '''
{
getUserNotificationSettings{
    id,
    userId,
    deviceHealthNotification,
    meetingUpdateNotification
}
}
'''

user_notification_response = {
    "data": {
        "getUserNotificationSettings": [
            {
                "id": "1",
                "userId": 1,
                "deviceHealthNotification": true,
                "meetingUpdateNotification": true
            }
        ]
        }
}

# when run for the first time for a user not already in the notifications table,
# the user is automatically added and the field is populated with the
# value provided.
update_user_notification_settings_query = '''
 mutation {
    updateNotification(
        deviceHealthNotification: true,
        meetingUpdateNotification: false) {
        notification {
            id
            userId
            deviceHealthNotification
            meetingUpdateNotification
        }
    }
}
'''

update_user_notification_settings_response = {
    "data": {
        "updateNotification": {
            "notification": {
                "id": "1",
                "userId": 1,
                "deviceHealthNotification": true,
                "meetingUpdateNotification": false
            }
        }
    }
}
