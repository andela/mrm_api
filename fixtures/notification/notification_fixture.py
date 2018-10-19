null = None
true = True
false = False

non_existent_user_notification_settings_query = '''
{
getUserNotificationSettings (userId:100){
    id,
    userId,
    deviceHealthNotification
}
}
'''

non_existent_user_notification_settings_response = {
    "errors": [
        {
            "message": "User not found",
            "locations": [
                {
                    "line": 2,
                    "column": 2
                }
            ],
            "path": [
                "getUserNotificationSettings"
            ]
        }
    ],
    "data": {
        "getUserNotificationSettings": null
    }
}

# when run for the first time for a user not already in the notifications table,
# the user is automatically added and the field is populated with the
# default value (True).
missing_user_notification_table_query = '''
{
getUserNotificationSettings (userId:1){
    id,
    userId,
    deviceHealthNotification
}
}
'''

missing_user_notification_table_response = {
    "data": {
        "getUserNotificationSettings": [
            {
                "id": "1",
                "userId": 1,
                "deviceHealthNotification": true
            }
        ]
        }
}

existing_user_notification_table_query = '''
{
getUserNotificationSettings (userId:1){
    id,
    userId,
    deviceHealthNotification
}
}
'''

existing_user_notification_table_response = {
    "data": {
        "getUserNotificationSettings": [
            {
                "id": "1",
                "userId": 1,
                "deviceHealthNotification": true
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
        deviceHealthNotification: true) {
        notification {
            id
            userId
            deviceHealthNotification
        }
    }
}
'''

update_user_notification_settings_response = {
    "data": {
        "updateNotification": {
            "notification": {
                "id": "1",
                "userId": 2,
                "deviceHealthNotification": true
            }
        }
    }
}
