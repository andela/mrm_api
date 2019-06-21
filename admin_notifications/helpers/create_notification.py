from flask_socketio import send, emit
from admin_notifications.models import AdminNotification
from manage import socketio
import celery


@celery.task(name="create-notification")
def create_notification(title, message, location_id):
    notification = AdminNotification(
        title=title,
        message=message,
        location_id=location_id,
        status="unread"
    )
    notification.save()
    new_notification = {"title": title, "message": message}
    return socketio.emit('notification', {'notification': new_notification}, broadcast=True)
