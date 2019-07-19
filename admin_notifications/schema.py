import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from datetime import datetime
from admin_notifications.models import AdminNotification as \
    AdminNotificationModel
from api.notification.models import Notification


class AdminNotifications(SQLAlchemyObjectType):
    """
        Returns the admin_notificationspayload
    """
    class Meta:
        model = AdminNotificationModel


class NotificationsList(graphene.ObjectType):
    """
        Class to return the types for Admin notifications
        \n- rooms: The rooms data
    """
    notifications = graphene.List(AdminNotifications)


class Query(graphene.ObjectType):
    all_unread_notifications = graphene.Field(
        NotificationsList,
        description="Returns a list of admin notifications"
    )

    @Auth.user_roles('Admin')
    def resolve_all_unread_notifications(self, info):
        notifications_on = Notification.query.filter_by(
            get_notifications=True
        ).first()
        if notifications_on:
            query = AdminNotifications.get_query(info)
            notifications = query.filter(
                AdminNotificationModel.status == "unread").all()
            return NotificationsList(notifications=notifications)
        raise GraphQLError("Notifications are turned off.")


class UpdateNotificationStatus(graphene.Mutation):
    """
        Class to update the status of a notification
    """

    class Arguments:
        notification_id = graphene.Int(required=True)
    notification = graphene.Field(AdminNotifications)

    @Auth.user_roles('Admin')
    def mutate(self, info, notification_id):
        query = AdminNotifications.get_query(info)
        unread_notifications = query.filter(
            AdminNotificationModel.status == "unread")
        notification = unread_notifications.filter(
            AdminNotificationModel.id == notification_id).first()
        if not notification:
            raise GraphQLError("Notification is already read or not found.")
        notification.status = "read"
        notification.date_read = datetime.now()
        notification.save()
        return UpdateNotificationStatus(notification=notification)


class Mutation(graphene.ObjectType):
    update_notification_status = UpdateNotificationStatus.Field(
        description="Updates the status od a notification and takes the argument\
            \n- notification_id: The name of the room[required]")
