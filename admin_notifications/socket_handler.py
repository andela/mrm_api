from flask_socketio import send
from admin_notifications.models import AdminNotification
from flask import jsonify

def serialize_message(notification):
    return {
        "title": notification.title,
        "message": notification.message,
    }

def send_notifications():
    query = AdminNotification.query
    notifications = query.filter_by(status="unread").all()
    notifications = [serialize_message(notification) for notification in notifications]
    return send(notifications, broadcast=True)

def send_single_notification(title, message):
  notification = { "title": title, "message": message }
  return send(notification, broadcast=True)
