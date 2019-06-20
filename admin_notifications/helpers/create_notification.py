from flask_socketio import send
from admin_notifications.models import AdminNotification
from manage import socketio

def create_notification(title, message, location_id):
  notification = AdminNotification(
    title=title,
    message=message,
    location_id=location_id,
    status="unread"
  )
  notification.save()
  
  @socketio.on('notification')
  def send_notification():
    notification = { "title": title, "message": message }
    return send(notification, broadcast=True)





def create_notif_lol():
  return create_notification(title="twre3r", message="rerf3ef3rf3rf", location_id=1)
