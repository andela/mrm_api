import requests
import celery
from config import Config

"""
This function will call slack bot url
"""


@celery.task(name="notify-slack")
def notify_slack(event_id):
    responce = requests.get(url=Config.NOTIFY_URL + event_id)
    return(responce.status_code)
