import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.room.models import Room as RoomModel
from api.room_resource.schema import Resource
from utilities.utility import validate_empty_fields,update_entity_fields
from helpers.calendar.events import RoomSchedules


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel

class Calendar(graphene.ObjectType):
        events = graphene.String()
    

class Calendar(graphene.ObjectType):
        events = graphene.String()


class CreateRoom(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String(required=True)
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        floor_id = graphene.Int(required=True)
        calendar_id = graphene.String(required=True)
    room = graphene.Field(Room)

    def mutate(self, info, **kwargs):
        room = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)


class UpdateRoom(graphene.Mutation):
    class Arguments:
        room_id = graphene.Int()
        name = graphene.String()
        room_type = graphene.String()
        capacity = graphene.Int()
        image_url = graphene.String()
    room = graphene.Field(Room)

    def mutate(self, info, room_id, **kwargs):
        validate_empty_fields(**kwargs)

        query_room = Room.get_query(info)
        exact_room = query_room.filter(RoomModel.id == room_id).first()
        update_entity_fields(exact_room, **kwargs)

        exact_room.save()
        return UpdateRoom(room=exact_room)


class Query(graphene.ObjectType):
    all_rooms = graphene.List(Room)
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int()
    )
    room_schedule = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
    )


    def resolve_all_rooms(self, info):
        query = Room.get_query(info)
        return query.all()

    def resolve_get_room_by_id(self, info, room_id):
        query = Room.get_query(info)
        check_room = query.filter(RoomModel.id == room_id).first()
        if not check_room:
            raise GraphQLError("Room not found")
        return check_room

    def resolve_room_schedule(self, info, calendar_id, days):
        query = Room.get_query(info)
        check_calendar_id = query.filter(RoomModel.calendar_id == calendar_id).first()
        if not check_calendar_id:
            raise GraphQLError("Invalid CalendarId")
        room_schedule = RoomSchedules.get_room_schedules(self,calendar_id,days)
        return Calendar(
            events = room_schedule
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        query = Room.get_query(info)
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
            ).first()
        if not check_calendar_id:
            raise GraphQLError("Invalid CalendarId")
        room_schedule = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            events=room_schedule
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        query = Room.get_query(info)
        check_calendar_id = query.filter(RoomModel.calendar_id == calendar_id).first()
        if not check_calendar_id:
            raise GraphQLError("Invalid CalendarId")
        room_schedule = RoomSchedules.get_room_schedules(self,calendar_id,days)
        return Calendar(
            events = room_schedule
        )

class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()

