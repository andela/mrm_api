from .email_setup import SendEmail
from config import Config
from flask import render_template
from api.room.models import Room as RoomModel


class EmailNotification:
    """
    Send email notifications
    """
    def send_email_notification(
        self, **kwargs
    ):
        """
        send email notifications after a given activity has occured
        """
        recipients = [kwargs.get('email')]

        email = SendEmail(
            kwargs.get('subject'), recipients,
            render_template(
                kwargs.get('template'),
                location_name=kwargs.get('location_name'),
                user_name=kwargs.get('user_name'),
                room_name=kwargs.get('room_name'),
                event_title=kwargs.get('event_title'),
                event_reject_reason=kwargs.get('event_reject_reason')
            ))

        return email.send()

    def email_invite(self, email, admin):
        """
        send email invite for user to join converge
        """
        email = SendEmail(
            "Invitation to join Converge", [email],
            render_template('invite.html', name=admin,
                            domain=Config.DOMAIN_NAME)
            )

        return email.send()

    def event_cancellation_notification(
        self, event, room_id, event_reject_reason
    ):
        """
        send email notifications on event rejection
         :params
            - event: The event being rejected
            - room_id: Id of the room rejecting the event
            - event_reject_reason: Reason for rejecting the event
        """
        event_title = event['summary']
        email = event['organizer']['email']
        room = RoomModel.query.filter_by(id=room_id).first()
        room_name = room.name
        subject = 'Your room reservation was rejected'
        template = 'event_cancellation.html'
        return EmailNotification.send_email_notification(
            self, email=email, subject=subject, template=template,
            room_name=room_name, event_title=event_title,
            event_reject_reason=event_reject_reason
        )

    def send_admin_invite_email(self, user_email, user_name):
        """
        send email notification when an admin is added
            :params
                - user_email: the email of the user being added as an admin
                - user_name: the name of the user being added as an admin
        """
        subject = 'Converge - You have been added as an admin'
        template = 'admin_invite.html'

        return EmailNotification.send_email_notification(
            self,
            email=user_email,
            subject=subject,
            user_name=user_name,
            template=template
        )


notification = EmailNotification()
