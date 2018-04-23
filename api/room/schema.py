import graphene

from graphql import GraphQLError
from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

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
        # for field in kwargs:
        #     if not kwargs.get(field):
        #         raise GraphQLError(f"Room {field} is required field")
        room  = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    rooms = SQLAlchemyConnectionField(Room)
    equipments = SQLAlchemyConnectionField(Equipment)


class Mutation(graphene.ObjectType):
    create_room = CreateRoom.Field()
