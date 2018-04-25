import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.room_resource.models import Resource as ResourceModel


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel
        interfaces = (relay.Node, )

class CreateResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        room_id = graphene.Int()
    resource = graphene.Field(Resource)

    def mutate(self, info, **kwargs):
        resource = ResourceModel(**kwargs)
        resource.save()
        
        return CreateResource(resource=resource)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    resources = SQLAlchemyConnectionField(Resource)
    single_resource = relay.Node.Field(Resource)


class Mutation(graphene.ObjectType):
    create_resource = CreateResource.Field()
