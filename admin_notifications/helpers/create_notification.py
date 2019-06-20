from admin_notifications.models import AdminNotification
from api.location.models import Location
from datetime import datetime


def update_notification(notification_id):
    notification = AdminNotification.query.filter_by(id=notification_id).first()
    notification.date_received = datetime.now()
    notification.save()


def create_notification(title, message, location_id):
    """
    Create notifications in the database and emit them to the client
    """
    from manage import socketio
    location = Location.query.filter_by(id=location_id).first()
    location_name = location.name
    notification = AdminNotification(
        title=title,
        message=message,
        location_id=location_id,
        status="unread"
    )
    notification.save()
    new_notification = {"title": title, "message": message}
    return socketio.emit(
        f"notifications-{location_name}",
        {'notification': new_notification},
        broadcast=True,
        callback=update_notification(notification.id)
    )
