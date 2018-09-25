import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.room.models import Room as RoomModel
from api.office.models import Office
from api.block.models import Block
from api.floor.models import Floor
from helpers.calendar.events import RoomSchedules
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from helpers.auth.verify_ids_for_room import verify_ids
from helpers.auth.validator import assert_wing_is_required
from helpers.auth.validator import ErrorHandler
from helpers.auth.add_office import verify_attributes
from helpers.room_filter.room_filter import room_filter, room_join_office
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

        if 'block_id' in kwargs:
            exact_block = Block.query.filter_by(id=kwargs['block_id']).first()
            if not exact_block:
                raise GraphQLError("Block with such id does not exist")
            floor = Floor.query.filter_by(id=kwargs['floor_id']).first()
            if floor.block_id == kwargs['block_id']:
                admin_roles.create_rooms_update_delete_office(office_id)
                query = Room.get_query(info)
                exact_query = room_join_office(query)
                result = exact_query.filter(
                    Office.id == office_id,
                    RoomModel.name == kwargs.get('name'))
                if result.count() > 0:
                    ErrorHandler.check_conflict(self, kwargs['name'], 'Room')
                assert_wing_is_required(get_office.name, kwargs)
                kwargs.pop('block_id')
                room = RoomModel(**kwargs)
                room.save()
                return CreateRoom(room=room)
            raise GraphQLError(
                "Floor with such id does not exist in this block")
        raise GraphQLError(
            "Block id is required")


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


class Query(graphene.ObjectType):
    all_rooms = graphene.Field(
        PaginatedRooms,
        page=graphene.Int(),
        per_page=graphene.Int(),
        capacity=graphene.Int(),
        resources=graphene.String(),
        location=graphene.String()
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int()
    )

    get_room_by_name = graphene.List(
        Room,
        name=graphene.String()
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int(),
    )

    room_schedule = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
    )
    room_occupants = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
    )

    def resolve_all_rooms(self, info, **kwargs):
        response = PaginatedRooms(**kwargs)
        return response

    def resolve_get_room_by_id(self, info, room_id):
        query = Room.get_query(info)
        check_room = query.filter(RoomModel.id == room_id).first()
        if not check_room:
            raise GraphQLError("Room not found")
        return check_room

    def resolve_get_room_by_name(self, info, name):
        query = Room.get_query(info)
        if name == "":
            raise GraphQLError("Please input Room Name")
        check_room_name = list(query.filter(RoomModel.name.ilike("%" + name + "%")).all())   # noqa: E501
        if not check_room_name:
            raise GraphQLError("Room not found")
        return check_room_name

    def resolve_room_occupants(self, info, calendar_id, days):
        query = Room.get_query(info)
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
        ).first()
        if not check_calendar_id:
            raise GraphQLError("Invalid CalendarId")
        room_occupants = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            occupants=room_occupants[0]
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        query = Room.get_query(info)
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
        ).first()
        if not check_calendar_id:
            raise GraphQLError("CalendarId given not assigned to any room on converge")  # noqa: E501
        room_schedule = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            events=room_schedule[1]
        )


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
    delete_room = DeleteRoom.Field()
