import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
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


class DeleteResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        resource_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    def mutate(self, info, name, resource_id, **kwargs):
        query_room_resource = Resource.get_query(info)
        exact_room_resource = query_room_resource.filter(
            ResourceModel.id == resource_id).first()

        exact_room_resource.delete()
        return DeleteResource(resource=exact_room_resource)


class Query(graphene.ObjectType):
    resources = graphene.List(Resource)

    def resolve_resources(self, info):
        query = Resource.get_query(info)
        return query.all()


class Mutation(graphene.ObjectType):

    create_resource = CreateResource.Field()
    delete_resource = DeleteResource.Field()
