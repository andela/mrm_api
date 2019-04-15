from graphql import GraphQLError

from api.location.models import Location
from api.room.models import Room as RoomModel
from helpers.auth.user_details import get_user_from_db
from helpers.room_filter.room_filter import (
    location_join_room)
from utilities.utility import StateType


class Admin_roles():

    def create_rooms_update_delete_location(self, kwargs):
        admin_details = get_user_from_db()
        location = Location.query.filter_by(id=kwargs['location_id']).first()
        if admin_details.location != location.name:
            raise GraphQLError("You are not authorized to make changes in " + location.name)  # noqa: E501

    def verify_admin_location(self, location_id):
        admin_details = get_user_from_db()
        location = Location.query.filter_by(id=location_id).first()
        if admin_details.location != location.name:
            raise GraphQLError(
                "You are not authorized to make changes in " + location.name
            )

    def update_delete_rooms_create_resource(self, room_id):
        admin_details = get_user_from_db()
        location_query = location_join_room()
        room_location = location_query.filter(
            RoomModel.id == room_id, RoomModel.state == "active").first()
        if admin_details.location != room_location.name:
            raise GraphQLError("You are not authorized to make changes in " + room_location.name)  # noqa: E501

    def user_location_for_analytics_view(self):
        """
        Return admin's location for viewing analytics data
        """
        admin_details = get_user_from_db()
        location = Location.query.filter_by(
             name=admin_details.location
        ).first()
        if location:
            if location.state != StateType.active:
                raise GraphQLError('Location is not active')
            return location.id
        raise GraphQLError('Your location does not exist')


admin_roles = Admin_roles()
