import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from admin_notifications.models import AdminNotification as AdminNotificationModel
from api.notification.models import Notification


class AdminNotifications(SQLAlchemyObjectType):
    """
       Returns admin notification payload
    """
    class Meta:
        model = AdminNotificationModel


class NotificationsList(graphene.ObjectType):
    """
       Class to return admin notifications.
    """
    notifications = graphene.List(AdminNotifications)


class Query(graphene.ObjectType):
    all_unread_notifications = graphene.Field(
        NotificationsList,
        description="Returns a list of admin notifications"
    )

    @Auth.user_roles('Admin')
    def resolve_all_unread_notifications(self, info):
        notifications_turned_on = Notification.query.filter_by(
            set_notifications_settings=True
        ).first()
        if notifications_turned_on:
            query = AdminNotifications.get_query(info)
            notifications = query.filter(
                AdminNotificationModel.status == "unread").all()
            return NotificationsList(notifications=notifications)
        raise GraphQLError("Notifications are turned off.")
