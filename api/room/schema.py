import graphene

from graphene import  Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from api.room.models import Room as RoomModel
from api.room_resource.schema import Resource

class Room(SQLAlchemyObjectType):
    
    class Meta:
        model = RoomModel


class CreateRoom(graphene.Mutation):
    
    class Arguments:
        name = graphene.String(required=True)
        room_type = graphene.String(required=True)
        capacity = graphene.Int(required=True)
        floor_id = graphene.Int(required=True)
    room = graphene.Field(Room)

    def mutate(self, info, **kwargs):
        room  = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)


class Query(graphene.ObjectType):
    rooms = graphene.List(Room)
    resource = graphene.List(Resource)
    get_room_by_id = graphene.List(
        lambda:Room,
        room_id = graphene.Int()
        )

    def resolve_rooms(self,info):
        query = Room.get_query(info)
        return query.all()

    def resolve_get_room_by_id(self,info,room_id):
        query =Room.get_query(info) 
        check_room = query.filter(RoomModel.id ==room_id).first()
        if not check_room:
            raise GraphQLError("Room not found")
        result = query.filter(RoomModel.id == room_id)
        return result

class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
   
