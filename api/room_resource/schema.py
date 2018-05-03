import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.room_resource.models import Resource as ResourceModel
from helpers.database import db_session


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel
        interfaces = (relay.Node, )

class CreateResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        room_id = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    def mutate(self, info, **kwargs):
        resource = ResourceModel(**kwargs)
        resource.save()
        
        return CreateResource(resource=resource)

class DeleteResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        resource_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    def mutate(self, info,name,resource_id, **kwargs):
        query_room_resource = Resource.get_query(info)
        exact_room_resource = query_room_resource.filter(ResourceModel.id == resource_id).first()
        
        exact_room_resource.delete()
        return DeleteResource(resource=exact_room_resource)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    room_resource = SQLAlchemyConnectionField(Resource)

class Mutation(graphene.ObjectType):

    create_resource = CreateResource.Field()
    delete_resource = DeleteResource.Field()
