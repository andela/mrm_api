import graphene

<<<<<<< HEAD
from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from mrm_api.models import (
    Room as RoomModel, Equipment as EquipmentModel,Utility)


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
        type_of_room = graphene.String()
        capacity = graphene.Int()
        floor_id = graphene.Int()
    room = graphene.Field(Room)

    def mutate(self, info, **kwargs):
        room  = RoomModel(**kwargs)
        room.save()

        return CreateRoom(room=room)
    
class UpdateRoom(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        type_of_room = graphene.String()
        capacity = graphene.Int()
        new_name = graphene.String()
        

    room = graphene.Field(Room)
    
    def mutate(self, info,name, **kwargs):
        query_room = Room.get_query(info)
        exact_room = query_room.filter(RoomModel.name == name).first()

        if kwargs.get("new_name"):
            exact_room.name = kwargs["new_name"]
        if kwargs.get("type_of_room"):
            exact_room.type_of_room = kwargs["type_of_room"]
        if kwargs.get("capacity"):
            exact_room.capacity = kwargs["capacity"]
            print(kwargs["capacity"])

        exact_room.save()
        return UpdateRoom(room=exact_room)



class Query(graphene.ObjectType):
    node = relay.Node.Field()
    rooms = SQLAlchemyConnectionField(Room)
    equipments = SQLAlchemyConnectionField(Equipment)


class Mutations(graphene.ObjectType):
    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()

schema = Schema(query=Query, mutation=Mutations)

import api.room.schema


class Query(
    api.room.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

