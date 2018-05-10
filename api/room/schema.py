import graphene

from graphene import  Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)
from graphql import GraphQLError
from api.room.models import Room as RoomModel
<<<<<<< HEAD
from api.room_resource.schema import Resource
=======
from api.equipment.schema import Equipment
>>>>>>> d82422178efb2d93cadff71d0c311879ba5a7f0a
from utilities.utility import validate_empty_fields

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

class UpdateRoom(graphene.Mutation):

    class Arguments:
        room_id = graphene.Int()
        room_type = graphene.String()
        capacity = graphene.Int()
        name = graphene.String()
        

    room = graphene.Field(Room)
    
    def mutate(self, info, room_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_room = Room.get_query(info)
        exact_room = query_room.filter(RoomModel.id == room_id).first()

        if kwargs.get("name"):  
            exact_room.name = kwargs["name"]
        if kwargs.get("room_type"):
            exact_room.room_type = kwargs["room_type"]
        if kwargs.get("capacity"):
            exact_room.capacity = kwargs["capacity"]
            
        exact_room.save()
        return UpdateRoom(room=exact_room)


class Query(graphene.ObjectType):
    rooms = graphene.List(Room)
    resource = graphene.List(Resource)

    def resolve_rooms(self,info):
        query = Room.get_query(info)
        return query.all()

class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
