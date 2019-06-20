null = None

get_all_unread_notifications = '''
query{
    allUnreadNotifications{
        notifications{
            id
            title
            message
        }
    }
}
'''

get_all_unread_notifications_response = {
    "data": {
        "allUnreadNotifications": {
            "notifications": []
        }
    }
}

get_all_unread_notifications_notifications_off_response = {
    "errors": [
        {
            "message": "Notifications are turned off.",
            "locations": [
                {
                    "line": 3,
                    "column": 5
                }
            ],
            "path": [
                "allUnreadNotifications"
            ]
        }
    ],
    "data": {
        "allUnreadNotifications": null
    }
}
