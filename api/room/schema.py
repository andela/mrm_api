import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.room.models import Room as RoomModel
from utilities.utility import validate_empty_fields, update_entity_fields


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel


class CreateRoom(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String(required=True)
        capacity = graphene.Int(required=True)
        image_url = graphene.String()
        floor_id = graphene.Int(required=True)
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
    get_room_by_id = graphene.List(
        lambda: Room,
        room_id=graphene.Int()
    )

    def resolve_all_rooms(self, info):
        query = Room.get_query(info)
        return query.all()

    def resolve_get_room_by_id(self, info, room_id):
        query = Room.get_query(info)
        check_room = query.filter(RoomModel.id == room_id).first()
        if not check_room:
            raise GraphQLError("Room not found")
        result = query.filter(RoomModel.id == room_id)
        return result


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
