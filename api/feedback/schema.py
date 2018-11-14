import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.feedback.models import Feedback as FeedbackModel
from helpers.auth.authentication import Auth


class Feedback(SQLAlchemyObjectType):
    class Meta:
        model = FeedbackModel


class RoomFeedback(graphene.Mutation):
    class Arguments:
        cleanliness_rating = graphene.Int()
        room_id = graphene.Int(required=True)
    feedback = graphene.Field(Feedback)

    @Auth.user_roles('Default User', 'Admin')
    def mutate(self, info, **kwargs):
        pass


class Mutation(graphene.ObjectType):
    room_feedback = RoomFeedback.Field()
