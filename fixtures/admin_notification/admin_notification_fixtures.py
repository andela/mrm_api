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
