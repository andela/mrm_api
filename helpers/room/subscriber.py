import requests
import celery
from config import Config


@celery.task(name="add-room-to-push-services")
def add_room(calendar_id, firebase_token):
    requests.get(url=Config.MRM_PUSH_URL + "/add_room",
                 params={"calendar_id": calendar_id,
                         "firebase_token": firebase_token})


@celery.task(name="remove-room-from-push-services")
def remove_room(calendar_id):
    requests.delete(url=Config.MRM_PUSH_URL + "/delete_room",
                    params={"calendar_id": calendar_id})


@celery.task(name="update-room-token")
def update_room_token(calendar_id, firebase_token):
    requests.get(url=Config.MRM_PUSH_URL + "/token",
                 params={"calendar_id": calendar_id,
                         "firebase_token": firebase_token})
