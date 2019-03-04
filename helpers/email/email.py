from .email_setup import SendEmail
from config import Config
from flask import render_template


def send_email_notification(admin_email, location_name, user_name):
    # send the email
    recipients = [admin_email]

    email = SendEmail(
        'A new location has been added', recipients,
        render_template(
            'location_success.html',
            location_name=location_name,
            user_name=user_name
        ))

    return email.send()


def email_invite(email, admin):
    email = SendEmail(
        "Invitation to join Converge", [email],
        render_template('invite.html', name=admin, domain=Config.DOMAIN_NAME))

    return email.send()
