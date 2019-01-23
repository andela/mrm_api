import graphene
from helpers.calendar.credentials import Credentials
from flask import jsonify
from pyfcm import FCMNotification
import uuid
import os

notification_url = (os.getenv('NOTIFICATION_URL')
                    if os.getenv('APP_SETTINGS') == 'production'
                    else os.getenv('DEV_NOTIFICATION_URL'))

push_service = FCMNotification(api_key=os.getenv('FCM_API_KEY'))


class NotificationChannelPerRoom(graphene.ObjectType):
    expiration = graphene.String()
    id = graphene.String()
    kind = graphene.String()
    resourceId = graphene.String()
    resourceUri = graphene.String()


class PushNotification():

    def create_channels(self, all_rooms):
        request_body = {
            "id": None,
            "type": "web_hook",
            "address": notification_url
        }
        service = Credentials.set_api_credentials(self)
        channels = []
        for room in all_rooms:
            request_body['id'] = str(uuid.uuid4())
            channel = service.events().watch(
                calendarId=room.calendar_id,
                body=request_body).execute()
            channel_created = NotificationChannelPerRoom(
                expiration=channel['expiration'],
                id=channel['id'],
                kind=channel['kind'],
                resourceId=channel['resourceId'],
                resourceUri=channel['resourceUri'])
            channels.append(channel_created)
        return channels

    def send_notifications(self):
        result = push_service.notify_single_device(
            registration_id=os.getenv('DEVICE_REGISTRATION_ID'),
            message_body="success")
        return jsonify(result)
