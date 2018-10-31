from flask_mail import Message, Mail
from config import Config
import celery


class SendEmail:
    """
    "Encapsulates an email message.

    :param subject: email subject header
    :param recipients: list of email addresses
    :param body: plain text message
    :param html: HTML message
    :param sender: email sender address
    """

    def __init__(
            self,
            subject,
            recipients,
            template,
    ):
        self.subject = subject
        self.recipients = recipients
        self.template = template
        self.sender = Config.MAIL_USERNAME
        self.message = Message(
            subject=self.subject,
            recipients=self.recipients,
            html=self.template,
            sender=self.sender)

    @celery.task
    def send_async_email(msg_dict):
        mail = Mail()
        msg = Message()
        msg.__dict__.update(msg_dict)
        mail.send(msg)

    def send(self):
        try:
            msg = self.message.__dict__
            self.send_async_email.apply_async(args=[msg])
            return True
        except Exception as e:
            print(e)
            return False
