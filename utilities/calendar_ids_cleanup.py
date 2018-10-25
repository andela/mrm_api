import graphene
from helpers.calendar.credentials import Credentials
from api.room.models import Room as RoomModel
from helpers.auth.authentication import Auth
from helpers.calendar.analytics_helper import CommonAnalytics


class DeleteResponse(graphene.ObjectType):
    response = graphene.String()
    rooms = graphene.List(graphene.String)


class Query(graphene.ObjectType):
    validate_rooms_calendar_ids = graphene.Field(DeleteResponse)

    @Auth.user_roles('Admin')
    def resolve_validate_rooms_calendar_ids(self, info):
        '''
        Validates the calendar IDs of all rooms in the database.
        Deletes all rooms with invalid calendar IDs.
        '''
        query = RoomModel.query
        calendar_ids = CommonAnalytics.get_calendar_id_name(self, query)
        service = Credentials.set_api_credentials(self)

        invalid_rooms = []
        message = "All rooms have valid calendar IDs"
        for cal in calendar_ids:
            try:
                service.events().list(calendarId=cal['calendar_id']).execute()
            except Exception:
                exact_room = query.filter(
                    RoomModel.calendar_id == cal['calendar_id']).first()
                exact_room.delete()
                invalid_rooms.append(cal['name'])
                message = "All rooms with invalid calendar IDs have been deleted"  # noqa E501
        response = DeleteResponse(
            response=message,
            rooms=invalid_rooms)
        return response
