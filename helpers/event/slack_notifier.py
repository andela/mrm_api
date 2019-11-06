import requests
import celery
from config import Config


@celery.task(name="notify-slack")
def notify_slack(event_id, organizer_email, room_id):
    """
    This function calls the slack BOT URL
    and notifies the organizer.
    """
    params_data = {
        "event_id": event_id,
        "organizer_email": organizer_email,
        "room_id": room_id
    }
    response = requests.get(url=Config.NOTIFY_URL, params=params_data)
    return(response.status_code)
