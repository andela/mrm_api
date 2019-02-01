import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from helpers.calendar.analytics_helper import CommonAnalytics
from helpers.calendar.events import RoomSchedules
from api.events.models import Events as EventsModel
from api.room.models import Room as RoomModel
from api.room.schema_query import PaginatedRooms


class Events(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel

    def check_status(self, info, **kwargs):
        try:
            room_id = RoomModel.query.filter_by(calendar_id=kwargs['calendar_id']).first().id  # noqa: E501
            if EventsModel.query.filter_by(
                    event_id=kwargs['event_id'],
                    room_id=room_id).count() > 0:
                raise GraphQLError("You cannot perform this action")
            return room_id

        except AttributeError:
            raise GraphQLError(
                "This Calendar ID is not registered on Converge.")


class CalendarEvents(graphene.ObjectType):
    event_id = graphene.String()
    start_date = graphene.String()
    end_date = graphene.String()
    event_title = graphene.String()
    recurring_event_id = graphene.String()
    room_name = graphene.String()


class RecurringEvents(graphene.ObjectType):
    day = graphene.String()
    events = graphene.List(CalendarEvents)


class Query(graphene.ObjectType):
    rooms = graphene.Field(PaginatedRooms, days=graphene.Int(),)
    all_recurring_events = graphene.Field(
        RecurringEvents,
        date=graphene.String(required=True),
        )

    def resolve_all_recurring_events(self, info, **kwargs):
        query = RoomModel.query
        start_date, end_date = CommonAnalytics().convert_dates(
            kwargs["date"], None)
        day = kwargs["date"]
        events = RoomSchedules().get_all_recurring_events(
            query, start_date, end_date)
        all_recurring_events = []
        for event in events:
            start_date = event["start_date"]
            end_date = event["end_date"]
            recurring_event = CalendarEvents(
                start_date=start_date,
                end_date=end_date,
                room_name=event["room_name"],
                event_title=event["event_summary"],
                recurring_event_id=event["recurring_event_id"],
                event_id=event["event_id"]
            )
            all_recurring_events.append(recurring_event)
        return RecurringEvents(
            day=day,
            events=all_recurring_events
        )


class EventList(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        pass


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
