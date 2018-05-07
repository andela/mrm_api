import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)
from graphql import GraphQLError
from api.room.models import Room as RoomModel
from api.equipment.schema import Equipment

class Room(SQLAlchemyObjectType):
    
    class Meta:
        model = RoomModel
        interfaces = (relay.Node, )


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
        name = graphene.String()
        room_type = graphene.String()
        capacity = graphene.Int()
        new_name = graphene.String()
        

    room = graphene.Field(Room)
    
    def mutate(self, info,name, **kwargs):
        query_room = Room.get_query(info)
        exact_room = query_room.filter(RoomModel.name == name).first()

        if kwargs.get("new_name"):
            exact_room.name = kwargs["new_name"]
        if kwargs.get("room_type"):
            exact_room.room_type = kwargs["room_type"]
        if kwargs.get("capacity"):
            exact_room.capacity = kwargs["capacity"]
            
        exact_room.save()
        return UpdateRoom(room=exact_room)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    rooms = SQLAlchemyConnectionField(Room)
    equipments = graphene.List(Equipment)
    get_room_by_id = graphene.List(
        lambda:Room,
        room_id = graphene.Int()
        )

    def resolve_get_room_by_id(self,info,room_id):
        query =Room.get_query(info) 
        result = query.filter(RoomModel.id == room_id)
        return result

class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
