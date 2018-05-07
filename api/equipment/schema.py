import graphene

from graphene import  Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.equipment.models import Equipment as EquipmentModel
from utilities.utility import validate_empty_fields


class Equipment(SQLAlchemyObjectType):
    
    class Meta:
        model = EquipmentModel

class Query(graphene.ObjectType):
    equipment = graphene.List(Equipment)

    def resolve_equipment(self,info):
        query = Equipment.get_query(info)
        return query.all()


class UpdateRoomResource(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        room_id = graphene.Int()
        resource_id = graphene.Int()

    equipment = graphene.Field(Equipment)
    def mutate(self,info,room_id,resource_id,**kwargs):
        validate_empty_fields(**kwargs)

        query = Equipment.get_query(info)

        exact_room = query.filter(EquipmentModel.room_id == room_id).first()
        if not exact_room:
            raise AttributeError("RoomId not found")

        exact_resource = query.filter(EquipmentModel.id == resource_id).first()
        if not exact_resource:
            raise AttributeError("ResourceId not found")

        if kwargs.get("name"):
            exact_resource.name = kwargs["name"]

        exact_room.save()
        return UpdateRoomResource(equipment = exact_resource)


class Mutation(graphene.ObjectType):
    update_room_resource = UpdateRoomResource.Field()