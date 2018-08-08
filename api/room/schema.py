import graphene
from math import ceil

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.room.models import Room as RoomModel
from api.office.models import Office
from helpers.calendar.events import RoomSchedules
from helpers.calendar.calendar import check_calendar_id
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.verify_ids_for_room import verify_ids
from helpers.auth.check_office_name import assert_wing_is_required
from helpers.auth.add_office import verify_attributes


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel


class Calendar(graphene.ObjectType):
    events = graphene.String()
    occupants = graphene.String()


class CreateRoom(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String(required=True)
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        floor_id = graphene.Int(required=True)
        calendar_id = graphene.String(required=True)
        office_id = graphene.Int()
        wing_id = graphene.Int()
    room = graphene.Field(Room)

    @Auth.user_roles('Admin')
    def mutate(self, info, office_id, **kwargs):
        verify_attributes(kwargs)
        verify_ids(kwargs, office_id)
        get_office = Office.query.filter_by(id=office_id).first()
        assert_wing_is_required(get_office.name, kwargs)
        room = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)


class PaginatedRooms(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    rooms = graphene.List(Room)

    def __init__(self, **kwargs):
        self.page = kwargs.pop('page', None)
        self.per_page = kwargs.pop('per_page', None)
        self.query_total
        self.pages

    def resolve_rooms(self, info):
        page = self.page
        per_page = self.per_page
        query = Room.get_query(info)
        if not page:
            return query.all()

        if page:
            if page < 1:
                return GraphQLError("No page requested")

            page = page - 1
            self.query_total = query.count()
            result = query.limit(per_page).offset(page*per_page)
            if result.count() == 0:
                return GraphQLError("No more resources")
            return result

    def resolve_pages(self, pages):
        if self.per_page:
            self.pages = ceil(self.query_total / self.per_page)
        pages = self.pages
        return pages

    def resolve_has_next(self, has_next):
        if self.page:
            page = self.page
            pages = self.pages
            pages = self.resolve_pages(pages)
            if page < pages:
                has_next = True
            else:
                has_next = False
        return has_next

    def resolve_has_previous(self, has_previous):
        if self.page:
            page = self.page
            pages = self.resolve_pages(self.pages)
            if (page > 1) and (pages > 1) and (page <= pages):
                has_previous = True
            else:
                has_previous = False

        return has_previous


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
            raise GraphQLError("RoomId not found")
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
            raise GraphQLError("RoomId not found")

        exact_room.delete()
        return DeleteRoom(room=exact_room)


class Query(graphene.ObjectType):
    all_rooms = graphene.Field(PaginatedRooms, page=graphene.Int(),
                               per_page=graphene.Int())
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int()
        )

    get_room_by_name = graphene.List(
        Room,
        name=graphene.String()
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
        result = check_calendar_id(info, calendar_id)
        if not result:
            raise GraphQLError("Invalid CalendarId")
        room_occupants = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            occupants=room_occupants[0]
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        result = check_calendar_id(info, calendar_id)
        if not result:
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
