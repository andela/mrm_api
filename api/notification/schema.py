import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.user.models import User
from helpers.auth.authentication import Auth
from api.notification.models import Notification as NotificationModel
from helpers.auth.user_details import get_user_from_db


class Notification(SQLAlchemyObjectType):
    class Meta:
        model = NotificationModel


class Query(graphene.ObjectType):

    get_user_notification_settings = graphene.List(
        lambda: Notification, user_id=graphene.Int(required=True))

    def resolve_get_user_notification_settings(self, info, user_id):
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise GraphQLError("User not found")
        query = Notification.get_query(info)
        notification = query.filter(
            NotificationModel.user_id == user_id).first()
        if not notification:
            notification = NotificationModel(user_id=user_id)
            notification.save()
        return [notification]  # makes the response iterable


class UpdateNotification(graphene.Mutation):
    class Arguments:
        device_health_notification = graphene.Boolean(required=True)

    notification = graphene.Field(Notification)

    @Auth.user_roles('Default User', 'Admin')
    def mutate(self, info, **kwargs):
        user = get_user_from_db()
        notification = NotificationModel.query.filter_by(
            user_id=user.id).first()
        if not notification:
            notification = NotificationModel(user_id=user.id)
        notification.device_health_notification = kwargs[
            'device_health_notification']
        notification.save()

        return UpdateNotification(notification=notification)


class Mutation(graphene.ObjectType):
    update_notification = UpdateNotification.Field()
