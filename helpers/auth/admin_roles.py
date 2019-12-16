from api.location.models import Location
from api.room.models import Room as RoomModel
from helpers.auth.user_details import get_user_from_db
from helpers.room_filter.room_filter import (
    location_join_room)
from utilities.utility import StateType
from api.bugsnag_error import return_error


class Admin_roles():

    def create_rooms_update_delete_location(self, kwargs):
        admin_details = get_user_from_db()
        location = Location.query.filter_by(id=kwargs['location_id']).first()
        if admin_details.location != location.name:
            return_error.report_errors_bugsnag_and_graphQL("You are not authorized to make changes in " + location.name)  # noqa: E501

    def verify_admin_location(self, location_id):
        admin_details = get_user_from_db()
        location = Location.query.filter_by(id=location_id).first()
        if admin_details.location != location.name:
            return_error.report_errors_bugsnag_and_graphQL(
                "You are not authorized to make changes in " + location.name
            )

    def update_delete_rooms_create_resource(self, room_id):
        admin_details = get_user_from_db()
        location_query = location_join_room()
        room_location = location_query.filter(
            RoomModel.id == room_id, RoomModel.state == "active").first()
        if admin_details.location != room_location.name:
            return_error.report_errors_bugsnag_and_graphQL("You are not authorized to make changes in " + room_location.name)  # noqa: E501

    def user_location_for_analytics_view(self, location_name=False):
        """
        Return admin's location for viewing analytics data
        """
        admin_details = get_user_from_db()
        location = Location.query.filter_by(
            name=admin_details.location
        ).first()
        if not location:
            return_error.report_errors_bugsnag_and_graphQL(
                'Your location does not exist')
        if location.state != StateType.active:
            return_error.report_errors_bugsnag_and_graphQL(
                'Location is not active')
        if location_name:
            return location.name
        return location.id


admin_roles = Admin_roles()
