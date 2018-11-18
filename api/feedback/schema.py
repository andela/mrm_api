import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.feedback.models import Feedback as FeedbackModel
from helpers.auth.authentication import Auth
from utilities.utility import validate_empty_fields
from helpers.auth.user_details import get_user_from_db
from graphql import GraphQLError
from api.room.schema import Room


class Feedback(SQLAlchemyObjectType):
    class Meta:
        model = FeedbackModel


class CreateFeedback(graphene.Mutation):
    class Arguments:
        room_id = graphene.Int(required=True)
        overall_rating = graphene.String()
        cleanliness_rating = graphene.String()
        comments = graphene.String()
    feedback = graphene.Field(Feedback)

    @Auth.user_roles('Default User')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        rating_values = ["Excellent", "Very Good", "Good", "Average", "Poor"]
        ratings = ["comments", "overall_rating", "cleanliness_rating"]

        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")

        if not set(ratings).intersection(kwargs):
            raise GraphQLError("Ensure to give at least one feedback input")
        ratings.pop(0)

        for feedback in kwargs:
            if feedback in ratings:
                if kwargs[feedback] not in rating_values:
                    raise GraphQLError("Invalid rating, only " + ', '.join(rating_values)+ " ratings allowed")  # noqa

        user = get_user_from_db()
        feedback = FeedbackModel(**kwargs, user_id=user.id)
        feedback.save()
        return CreateFeedback(feedback=feedback)


class Mutation(graphene.ObjectType):
    create_feedback = CreateFeedback.Field()
