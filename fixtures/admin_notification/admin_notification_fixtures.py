null = None

get_all_unread_notifications = '''
query {
    allUnreadNotifications{
      notifications {
        title
        message
        id
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

get_all_unread_notifications_settings_false = '''
query {
    allUnreadNotifications{
      notifications {
        id
        title
        message
      }
    }
}
'''

get_all_unread_notifications_response_on_false = {
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

change_notification_status_unexistent_id = '''
mutation {
  updateNotificationStatus(notificationId: 260){
    notification {
      id
      title
      message
    }
  }
}
'''

change_notification_status_unexistent_id_response = {
    "errors": [
      {
        "message": "Notification is already read or not found.",
        "locations": [
          {
            "line": 3,
            "column": 3
          }
        ],
        "path": [
          "updateNotificationStatus"
        ]
      }
    ],
    "data": {
      "updateNotificationStatus": null
    }
}
