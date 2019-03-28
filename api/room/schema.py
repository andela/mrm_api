import requests
import graphene
from sqlalchemy import func
from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from config import Config
from api.room.models import Room as RoomModel
from api.tag.models import Tag as TagModel
from api.office.models import Office
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from utilities.verify_ids_for_room import verify_ids
from utilities.validator import (
    ErrorHandler,
    assert_wing_is_required,
    assert_block_id_is_required)
from helpers.room_filter.room_filter import (
    room_filter,
    room_join_office)
from helpers.pagination.paginate import Paginate, validate_page


class Room(SQLAlchemyObjectType):
    """
        Autogenerated return type of a room
    """
    class Meta:
        model = RoomModel


def save_room_tags(room, room_tags):
    # save room tags
    missing_tags = ""
    for tag in room_tags:
        room_tag = TagModel.query.filter_by(id=tag).first()
        if not room_tag:
            missing_tags += str(tag)+" "
        room.room_tags.append(room_tag)
    if missing_tags:
        raise GraphQLError("Tag id {}not found".format(missing_tags))
    room.save()


class RatioOfCheckinsAndCancellations(graphene.ObjectType):
    """
        Query to get the ratio of checkins to cancellations and takes the
            arguments \n- room_name: The name of the room
                \n- checkins: The number of the event checkins in a room
                \n- cancellations: The number of the even cacellations in a room
                \n- bookings: The number of the room bookings
                \n- checkins_percentage: The percentage of room checkins
                \n- cancellations_percentage: The percentage of room
                cancellations \n- app_bookings: The number of the room bookings
                    via app \n- app_bookings_percentage: The field with the
                        percentage of room bookings via app
    """
    room_id = graphene.Int()
    room_name = graphene.String()
    checkins = graphene.Int()
    cancellations = graphene.Int()
    bookings = graphene.Int()
    checkins_percentage = graphene.Float()
    cancellations_percentage = graphene.Float()
    app_bookings = graphene.Int()
    app_bookings_percentage = graphene.Float()


class Calendar(graphene.ObjectType):
    """
        Querry for the calendar events and accepts the arguments
        \n- events: The calendar events in a room
        \n- occupants: The number of occupants of a room
    """
    events = graphene.String()
    occupants = graphene.String()


class RoomFilter(graphene.ObjectType):
    """
        Class to filter room data and takes the argument
        \n- rooms: The rooms data
    """
    rooms = graphene.List(Room)


class BookingsAnalyticsCount(graphene.ObjectType):
    """
        Class to get the bookings analytics and takes the arguments
        \n- bookings: The number of room bookings
        \n- period: The duration tha a room is booked
    """
    bookings = graphene.Int()
    period = graphene.String()
    room_name = graphene.String()


class CreateRoom(graphene.Mutation):
    """
        Return payload when creating a room
    """
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String()
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        location_id = graphene.Int(required=True)
        floor_id = graphene.Int(required=True)
        calendar_id = graphene.String()
        office_id = graphene.Int(required=True)
        wing_id = graphene.Int()
        block_id = graphene.Int()
        cancellation_duration = graphene.Int()
        room_tags = graphene.List(graphene.Int)
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, office_id, **kwargs):
        validate_empty_fields(**kwargs)
        verify_ids(office_id, kwargs)
        get_office = Office.query.filter_by(id=office_id).first()

        admin_roles.create_rooms_update_delete_office(office_id)
        query = Room.get_query(info)
        active_rooms = query.filter(RoomModel.state == "active")
        query_result = [room for room in active_rooms
                        if room.calendar_id == kwargs.get('calendar_id')]
        if query_result:
            ErrorHandler.check_conflict(
                self, kwargs['calendar_id'], 'CalenderId')

        exact_query = room_join_office(active_rooms)
        result = exact_query.filter(
            Office.id == office_id,
            RoomModel.name == kwargs.get('name'),
            RoomModel.state == "active")
        if result.count():
            ErrorHandler.check_conflict(self, kwargs['name'], 'Room')
        assert_block_id_is_required(get_office.name, kwargs)
        assert_wing_is_required(get_office.name, kwargs)
        # remove block ID from kwargs, can't be saved in rooms model
        if kwargs.get('block_id'):
            kwargs.pop('block_id')
        room_tags = []
        if kwargs.get('room_tags'):
            room_tags = kwargs.pop('room_tags')
        room = RoomModel(**kwargs)
        save_room_tags(room, room_tags)
        return CreateRoom(room=room)


class PaginatedRooms(Paginate):
    """
        Return paginated rooms
    """
    rooms = graphene.List(Room)

    def resolve_rooms(self, info, **kwargs):
        page = self.page
        per_page = self.per_page
        filter_data = self.filter_data
        query = Room.get_query(info)
        exact_query = room_filter(query, filter_data)
        active_rooms = exact_query.filter(RoomModel.state == "active")
        if not page:
            return active_rooms.order_by(func.lower(RoomModel.name)).all()
        page = validate_page(page)
        self.query_total = active_rooms.count()
        result = active_rooms.order_by(func.lower(
            RoomModel.name)).limit(per_page).offset(page*per_page)
        if result.count() == 0:
            return GraphQLError("No more resources")
        return result


class UpdateRoom(graphene.Mutation):
    """
        Update a givem room
    """
    class Arguments:
        room_id = graphene.Int()
        name = graphene.String()
        room_type = graphene.String()
        capacity = graphene.Int()
        image_url = graphene.String()
        calendar_id = graphene.String()
        firebase_token = graphene.String()
        cancellation_duration = graphene.Int()
        room_tags = graphene.List(graphene.Int)
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, room_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_room = Room.get_query(info)
        active_rooms = query_room.filter(RoomModel.state == "active")
        room = active_rooms.filter(RoomModel.id == room_id).first()
        if not room:
            raise GraphQLError("Room not found")
        admin_roles.update_delete_rooms_create_resource(room_id)
        room_tags = []
        if kwargs.get('room_tags'):
            room_tags = kwargs.pop('room_tags')
        update_entity_fields(room, **kwargs)
        previous_tags = room.room_tags
        previous_tags.clear()
        save_room_tags(room, room_tags)
        return UpdateRoom(room=room)


class DeleteRoom(graphene.Mutation):
    """
        Delete a specific room using its room_id
    """

    class Arguments:
        room_id = graphene.Int(required=True)
        state = graphene.String()
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, room_id, **kwargs):
        query_room = Room.get_query(info)
        active_rooms = query_room.filter(RoomModel.state == "active")
        exact_room = active_rooms.filter(
            RoomModel.id == room_id).first()
        if not exact_room:
            raise GraphQLError("Room not found")
        exact_room.room_tags.clear()
        admin_roles.update_delete_rooms_create_resource(room_id)
        update_entity_fields(exact_room, state="archived", **kwargs)
        exact_room.save()
        return DeleteRoom(room=exact_room)


class UpdateFirebaseToken(graphene.Mutation):
    """
        Class to update the firebase token
    """

    class Arguments:
        room_id = graphene.Int(required=True)
        firebase_token = graphene.String(required=True)
    room = graphene.Field(Room)

    def mutate(self, info, room_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_room = Room.get_query(info)
        active_rooms = query_room.filter(RoomModel.state == "active")
        room = active_rooms.filter(RoomModel.id == room_id).first()
        if not room:
            raise GraphQLError("Room not found")
        update_entity_fields(room, **kwargs)
        room.save()
        requests.get(url=Config.MRM_PUSH_URL, params="hello")
        return UpdateFirebaseToken(room=room)


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field(
        description="Creates a new room and takes the arguments\
            \n- name: The name of the room[required]\
            \n- room_type: The type of the given room\
            \n- capacity: The number of peaople that the room can hold\
            [required]\n- image_url: The image url of the room\
            \n- location_id: The unique identifier of the location where the \
            room is found\n- floor_id: The unique identifier of the floor where\
            the room is found[required]\n- calendar_id: The unique identifier \
            of the calendar\n- office_id: The unique identifier of the office \
            where the room is found[required]\n- wing_id: The unique identifier\
            of the wing where the room is found\n- block_id: The unique \
                identifier of the block where the room is found\
            \n- cancellation_duration: The cancellation duration of a booking\
            \n- room_tags: The necessary tags associated with the room")
    update_room = UpdateRoom.Field(
        description="Updates a room taking the arguments \
            \n- room_id: Unique key identifier of a room\
            \n- name: The name of the room\
            \n- room_type: The type of the given room\
            \n- capacity: The number of peaople that the room can hold\
            \n- image_url: The image url of the room\
            \n- calendar_id: The unique identifier of the calendar\
            \n- firebase_token: Field with users firebase token\
            \n- cancellation_duration: The cancellation duration of a booking\
            \n- room_tags: The necessary tags associated with the room")
    delete_room = DeleteRoom.Field(
        description="Mutation to delete a room with arguments\
            \n- room_id: Unique key identifier of a room[required]\
            \n- state: Check if the room is active, archived or deleted")
    update_firebase_token = UpdateFirebaseToken.Field(
        description="Mutation to update firebase token and takes arguments\
            \n- room_id: Unique key identifier of a room[required]\
            \n- firebase_token: Field with users firebase token[required]")
