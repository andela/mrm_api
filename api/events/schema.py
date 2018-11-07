import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.events.models import Events as EventsModel
from api.room.models import Room


class Events(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel

    def check_status(self, info, **kwargs):
        try:
            room_id = Room.query.filter_by(calendar_id=kwargs['calendar_id']).first().id  # noqa: E501
            if EventsModel.query.filter_by(
                    event_id=kwargs['event_id'],
                    room_id=room_id).count() > 0:
                raise GraphQLError("This event already exists.")
            return room_id

        except AttributeError:
            raise GraphQLError(
                "This Calendar ID is not registered on Converge.")


class EventCheckin(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id = Events.check_status(self, info, **kwargs)
        new_event = EventsModel(
            event_id=kwargs['event_id'],
            room_id=room_id,
            event_title=kwargs['event_title'],
            start_time=kwargs['start_time'],
            end_time=kwargs['end_time'],
            checked_in=True,
            cancelled=False)
        new_event.save()

        return EventCheckin(event=new_event)


class CancelEvent(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id = Events.check_status(self, info, **kwargs)
        cancelled_event = EventsModel(
            event_id=kwargs['event_id'],
            room_id=room_id,
            event_title=kwargs['event_title'],
            start_time=kwargs['start_time'],
            end_time=kwargs['end_time'],
            checked_in=False,
            cancelled=True)
        cancelled_event.save()

        return CancelEvent(event=cancelled_event)


class Mutation(graphene.ObjectType):
    event_checkin = EventCheckin.Field()
    cancelled_event = CancelEvent.Field()
