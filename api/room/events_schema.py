import graphene
from api.room.schema import (Room)
from helpers.calendar.events import RoomSchedules
from helpers.pagination.paginate import ListPaginate
from helpers.calendar.analytics_helper import CommonAnalytics


class CalendarEvent(graphene.ObjectType):
    no_of_participants = graphene.Int()
    event_summary = graphene.String()
    start_time = graphene.String()
    end_time = graphene.String()
    room_name = graphene.String()
    event_id = graphene.String()


class DailyEvents(graphene.ObjectType):
    day = graphene.String()
    events = graphene.List(CalendarEvent)


class PaginatedEvents(graphene.ObjectType):
    """
        Paginated result for daily room events
        analytics
    """
    DailyRoomEvents = graphene.List(DailyEvents)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()


class Query(graphene.ObjectType):

    def resolve_analytics_for_daily_room_events(
        self, info, start_date, end_date, page=None, per_page=None
    ):
        start_date, end_date = CommonAnalytics().convert_dates(
            start_date, end_date
        )
        query = Room.get_query(info)
        all_events, all_dates = RoomSchedules().get_all_room_schedules(
            query, start_date, end_date
        )
        all_days_events = []
        for date in set(all_dates):
            daily_events = []
            for event in all_events:
                if date == event["date_of_event"]:
                    current_event = CalendarEvent(
                        no_of_participants=event["no_of_participants"],
                        event_summary=event["event_summary"],
                        start_time=event["start_time"],
                        end_time=event["end_time"],
                        room_name=event["room_name"],
                        event_id=event["event_id"]
                    )
                    daily_events.append(current_event)
            all_days_events.append(
                DailyEvents(
                    day=date,
                    events=daily_events
                )
            )
        if page and per_page:
            paginated_results = ListPaginate(
                iterable=all_days_events, per_page=per_page, page=page
            )
            current_page = paginated_results.current_page
            has_previous = paginated_results.has_previous
            has_next = paginated_results.has_next
            pages = paginated_results.pages
            return PaginatedEvents(
                DailyRoomEvents=current_page,
                has_next=has_next,
                has_previous=has_previous,
                pages=pages
            )
        return PaginatedEvents(
            DailyRoomEvents=all_days_events
        )
