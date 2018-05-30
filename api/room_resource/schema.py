import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

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


class Mutation(graphene.ObjectType):

    create_resource = CreateResource.Field()
