from flask import render_template

from flask_mail import Message, Mail

from config import Config
from api.user.models import User
import celery

mail = Mail()


@celery.task
def send_async_email(msg_dict):
    """
    Send office created email
    """
    msg = Message()
    msg.__dict__.update(msg_dict)
    mail.send(msg)


def office_created(new_office):
    # send the email
    users = User.query.all()
    recipients = [
        user.email for user in users if [
            user_role.role for user_role in user.roles
            if user_role.role == 'Admin'
        ]
    ]

    msg = Message(
        'A new office has been added',
        recipients=recipients,
        sender=Config.MAIL_USERNAME)
    msg.html = render_template('office_success.html', office_name=new_office)

    msg_dict = msg.__dict__
    try:
        send_async_email.apply_async(args=[msg_dict])
        return True
    except Exception as e:  # noqa
        return False
