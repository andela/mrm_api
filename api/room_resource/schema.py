import graphene

from graphql import GraphQLError
from graphene import  Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.room_resource.models import Resource as ResourceModel
from utilities.utility import validate_empty_fields


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel

class Query(graphene.ObjectType):
    resource = graphene.List(Resource)

    def resolve_resource(self,info):
        query = Resource.get_query(info)
        return query.all()


class UpdateRoomResource(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        room_id = graphene.Int()
        resource_id = graphene.Int()

    resource = graphene.Field(Resource)
    def mutate(self,info,room_id,resource_id,**kwargs):
        validate_empty_fields(**kwargs)

        query = Resource.get_query(info)

        exact_room = query.filter(ResourceModel.room_id == room_id).first()
        if not exact_room:
            raise GraphQLError("RoomId not found")

        exact_resource = query.filter(ResourceModel.room_id == room_id).filter (ResourceModel.id == resource_id).first()
        if not exact_resource:
            raise GraphQLError("ResourceId not found")

        if kwargs.get("name"):
            exact_resource.name = kwargs["name"]

        exact_room.save()
        return UpdateRoomResource(resource = exact_resource)


class Mutation(graphene.ObjectType):
    update_room_resource = UpdateRoomResource.Field()