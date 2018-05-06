import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.room_resource.models import Resource as ResourceModel


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel

class CreateResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        room_id = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    def mutate(self, info, **kwargs):
        resource = ResourceModel(**kwargs)
        resource.save()
        
        return CreateResource(resource=resource)

class Query(graphene.ObjectType):
    resources = graphene.List(Resource)
    get_resource_by_room_id = graphene.List(lambda: Resource, room_id = graphene.Int())
    
    def resolve_resources(self, info):
        query = Resource.get_query(info)
        return query.all()
    
    def resolve_get_resource_by_room_id(self, info, room_id):
        query = Resource.get_query(info)
        return query.filter(ResourceModel.room_id == room_id.frist())

class Mutation(graphene.ObjectType):
    create_resource = CreateResource.Field()
