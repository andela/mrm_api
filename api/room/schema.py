import graphene
from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.room.models import Room as RoomModel
from api.office.models import Office
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from helpers.auth.verify_ids_for_room import verify_ids, validate_block
from helpers.auth.validator import assert_wing_is_required, assert_block_id_is_required  # noqa: E501
from helpers.auth.validator import ErrorHandler
from helpers.auth.add_office import verify_attributes
from helpers.room_filter.room_filter import room_filter, room_join_office  # noqa: E501
from helpers.pagination.paginate import Paginate, validate_page


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel


class Calendar(graphene.ObjectType):
    events = graphene.String()
    occupants = graphene.String()


class RoomFilter(graphene.ObjectType):
    rooms = graphene.List(Room)


class CreateRoom(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String()
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        floor_id = graphene.Int(required=True)
        calendar_id = graphene.String()
        office_id = graphene.Int(required=True)
        wing_id = graphene.Int()
        block_id = graphene.Int()
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
        room = RoomModel(**kwargs)
        room.save()
        return CreateRoom(room=room)


class PaginatedRooms(Paginate):
    rooms = graphene.List(Room)

    def resolve_rooms(self, info, **kwargs):
        page = self.page
        per_page = self.per_page
        filter_data = self.filter_data
        query = Room.get_query(info)
        exact_query = room_filter(query, filter_data)
        if not page:
            return exact_query.all()
        page = validate_page(page)
        self.query_total = exact_query.count()
        result = exact_query.limit(per_page).offset(page*per_page)
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
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, room_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_room = Room.get_query(info)
        exact_room = query_room.filter(RoomModel.id == room_id).first()
        if not exact_room:
            raise GraphQLError("Room not found")

        admin_roles.update_delete_rooms_create_resource(room_id)
        update_entity_fields(exact_room, **kwargs)

        exact_room.save()
        return UpdateRoom(room=exact_room)


class DeleteRoom(graphene.Mutation):

    class Arguments:
        room_id = graphene.Int(required=True)
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, room_id, **kwargs):
        query_room = Room.get_query(info)
        exact_room = query_room.filter(
            RoomModel.id == room_id).first()
        if not exact_room:
            raise GraphQLError("Room not found")

        admin_roles.update_delete_rooms_create_resource(room_id)
        exact_room.delete()
        return DeleteRoom(room=exact_room)


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
    delete_room = DeleteRoom.Field()
