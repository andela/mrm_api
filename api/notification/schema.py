import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from helpers.auth.authentication import Auth
from api.notification.models import Notification as NotificationModel
from helpers.auth.user_details import get_user_from_db


class Notification(SQLAlchemyObjectType):
    class Meta:
        model = NotificationModel


class Query(graphene.ObjectType):
    get_user_notification_settings = graphene.List(Notification)

    def resolve_get_user_notification_settings(self, info):
        user = get_user_from_db()
        if user is None:
            raise GraphQLError("User not found")
        query = Notification.get_query(info)
        notification = query.filter(
            NotificationModel.user_id == user.id).first()
        if notification is None:
            notification = NotificationModel(user_id=user.id)
            notification.save()
        return [notification]  # makes the response iterable


class UpdateNotification(graphene.Mutation):
    class Arguments:
        device_health_notification = graphene.Boolean()
        meeting_update_notification = graphene.Boolean()
    notification = graphene.Field(Notification)

    @Auth.user_roles('Default User', 'Admin')
    def mutate(self, info, **kwargs):
        user = get_user_from_db()
        notification = NotificationModel.query.filter_by(
            user_id=user.id).first()
        if not notification:
            notification = NotificationModel(user_id=user.id)
        if 'device_health_notification' in kwargs:
            notification.device_health_notification = kwargs[
                'device_health_notification']
        if 'meeting_update_notification' in kwargs:
            notification.meeting_update_notification = kwargs[
                'meeting_update_notification']
        notification.save()

        return UpdateNotification(notification=notification)


class Mutation(graphene.ObjectType):
    update_notification = UpdateNotification.Field()
