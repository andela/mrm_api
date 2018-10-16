import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.events.models import Events as EventsModel
from api.room.models import Room


class Events(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel


class EventCheckin(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        try:
            room_id = Room.query.filter_by(calendar_id=kwargs['calendar_id']).first().id  # noqa: E501
            if EventsModel.query.filter_by(
                    event_id=kwargs['event_id'],
                    room_id=room_id).count() > 0:
                raise GraphQLError("This event already exists.")

            new_event = EventsModel(
                event_id=kwargs['event_id'],
                room_id=room_id,
                checked_in=True,
                cancelled=False)
            new_event.save()

            return EventCheckin(event=new_event)

        except AttributeError:
            raise GraphQLError(
                "This Calendar ID is not registered on Converge.")


class Mutation(graphene.ObjectType):
    event_checkin = EventCheckin.Field()
