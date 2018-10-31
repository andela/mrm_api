from .email_setup import SendEmail
from api.user.models import User
from config import Config
from flask import render_template


def office_created(new_office):
    # send the email
    users = User.query.all()
    recipients = [
        user.email for user in users if [
            user_role.role for user_role in user.roles
            if user_role.role == 'Admin'
        ]
    ]
    email = SendEmail(
        'A new office has been added', recipients,
        render_template('office_success.html', office_name=new_office))

    return email.send()


def email_invite(email, admin):
    email = SendEmail(
        "Invitaion to join Converge", [email],
        render_template('invite.html', name=admin, domain=Config.DOMAIN_NAME))

    return email.send()
