import graphene
from sqlalchemy import exc
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.events.models import Events as EventsModel
from helpers.calendar.events import RoomSchedules


class Events(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel


class EventCheckin(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        try:
            room_id = RoomSchedules().check_event_status(info, **kwargs)
            event = EventsModel.query.filter_by(
                start_time=kwargs['start_time'],
                event_id=kwargs['event_id']).scalar()
            if event is not None:
                event.checked_in = True
                event.save()
            else:
                event = EventsModel(
                    event_id=kwargs['event_id'],
                    room_id=room_id,
                    event_title=kwargs['event_title'],
                    start_time=kwargs['start_time'],
                    end_time=kwargs['end_time'],
                    checked_in=True,
                    cancelled=False)
                event.save()
            return EventCheckin(event=event)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class CancelEvent(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        try:
            room_id, event = check_event_in_db(
                self, info, "cancelled", **kwargs)
            if not event:
                event = EventsModel(
                    event_id=kwargs['event_id'],
                    room_id=room_id,
                    event_title=kwargs['event_title'],
                    start_time=kwargs['start_time'],
                    end_time=kwargs['end_time'],
                    checked_in=False,
                    cancelled=True)
                event.save()

            return CancelEvent(event=event)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


def check_event_in_db(instance, info, event_check, **kwargs):
    room_id = RoomSchedules().check_event_status(info, **kwargs)
    event = EventsModel.query.filter_by(
        start_time=kwargs['start_time'],
        event_id=kwargs['event_id']).scalar()
    if event and event_check == 'cancelled':
        event.cancelled = True
        event.save()
        return room_id, event
    elif event and event_check == 'checked_in':
        event.checked_in = True
        event.save()
        return room_id, event
    return room_id, event


class Mutation(graphene.ObjectType):
    event_checkin = EventCheckin.Field()
    cancel_event = CancelEvent.Field()
