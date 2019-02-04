import graphene
from sqlalchemy import func
from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.room.models import Room as RoomModel
from api.tag.models import Tag as TagModel
from api.office.models import Office
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from helpers.auth.verify_ids_for_room import verify_ids, validate_block
from helpers.auth.validator import (
    assert_wing_is_required,
    assert_block_id_is_required)
from helpers.auth.validator import ErrorHandler
from helpers.auth.add_office import verify_attributes
from helpers.room_filter.room_filter import (
    room_filter,
    room_join_office)
from helpers.pagination.paginate import Paginate, validate_page


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel


def save_room_tags(room, room_tags):
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
    room_name = graphene.String()
    checkins = graphene.Int()
    cancellations = graphene.Int()
    bookings = graphene.Int()
    checkins_percentage = graphene.Float()
    cancellations_percentage = graphene.Float()
    app_bookings = graphene.Int()
    app_bookings_percentage = graphene.Float()


class Calendar(graphene.ObjectType):
    events = graphene.String()
    occupants = graphene.String()


class RoomFilter(graphene.ObjectType):
    rooms = graphene.List(Room)


class BookingsAnalyticsCount(graphene.ObjectType):
    bookings = graphene.Int()
    period = graphene.String()


class CreateRoom(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String()
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        location_id = graphene.Int()
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
        verify_attributes(kwargs)
        verify_ids(office_id, kwargs)
        get_office = Office.query.filter_by(id=office_id).first()
        if not get_office:
            raise GraphQLError("No Office Found")

        admin_roles.create_rooms_update_delete_office(office_id)
        query = Room.get_query(info)
        exact_query = room_join_office(query)
        result = exact_query.filter(
            Office.id == office_id,
            RoomModel.name == kwargs.get('name'))
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Room')
        assert_block_id_is_required(get_office.name, kwargs)
        validate_block(office_id, kwargs)
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


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
    delete_room = DeleteRoom.Field()
