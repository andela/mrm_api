from .email_setup import SendEmail
from config import Config
from flask import render_template


def send_email_notification(admin_email, new_office):
    # send the email
    recipients = [admin_email]

    email = SendEmail(
        'A new office has been added', recipients,
        render_template('office_success.html', office_name=new_office))

    return email.send()


def email_invite(email, admin):
    email = SendEmail(
        "Invitaion to join Converge", [email],
        render_template('invite.html', name=admin, domain=Config.DOMAIN_NAME))

    return email.send()
