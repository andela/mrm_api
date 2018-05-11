import graphene

from graphql import GraphQLError
from graphene import  Schema
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.room_resource.models import Resource as ResourceModel
from utilities.utility import (
    validate_empty_fields,
    update_entity_fields,
    )


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
    def mutate(self, info, resource_id, **kwargs):
        validate_empty_fields(**kwargs)
        query = Resource.get_query(info)
        exact_resource = query.filter(ResourceModel.id == resource_id).first()
        
        if not exact_resource:
            raise GraphQLError("ResourceId not Found")
         
        update_entity_fields(exact_resource, **kwargs)
        exact_resource.save()
        return UpdateRoomResource(resource = exact_resource)


class Mutation(graphene.ObjectType):
    update_room_resource = UpdateRoomResource.Field()