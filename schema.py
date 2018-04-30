import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from models import (
    Room as RoomModel, Equipment as EquipmentModel)


class Room(SQLAlchemyObjectType):
    
    class Meta:
        model = RoomModel
        interfaces = (relay.Node, )


class Equipment(SQLAlchemyObjectType):
    
    class Meta:
        model = EquipmentModel
        interfaces = (relay.Node, )


class CreateRoom(graphene.Mutation):
    
    class Arguments:
        name = graphene.String()
        type = graphene.String()
        capacity = graphene.Int()
        floor_id = graphene.Int()
    room = graphene.Field(Room)

    def mutate(self, info, **kwargs):
        room  = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    rooms = SQLAlchemyConnectionField(Room)
    equipments = SQLAlchemyConnectionField(Equipment)


class Mutations(graphene.ObjectType):
    create_room = CreateRoom.Field()

schema = Schema(query=Query, mutation=Mutations)
