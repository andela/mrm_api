import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.room_resource.models import Resource as ResourceModel
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.authentication import Auth
from helpers.pagination.paginate import Paginate, validate_page


class Resource(SQLAlchemyObjectType):

    class Meta:
        model = ResourceModel


class PaginatedResource(Paginate):
    resources = graphene.List(Resource)

    def resolve_resources(self, info):
        page = self.page
        per_page = self.per_page
        unique = self.unique
        query = Resource.get_query(info)
        if not page:
            if unique:
                return query.distinct(ResourceModel.name).all()
            return query.all()
        page = validate_page(page)
        self.query_total = query.count()
        result = query.limit(per_page).offset(page*per_page)
        if result.count() == 0:
            return GraphQLError("No more resources")
        return result


class CreateResource(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        room_id = graphene.Int(required=True)
        quantity = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        resource = ResourceModel(**kwargs)
        resource.save()

        return CreateResource(resource=resource)


class UpdateRoomResource(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        room_id = graphene.Int()
        resource_id = graphene.Int()
        quantity = graphene.Int()
    resource = graphene.Field(Resource)

    @Auth.user_roles('Admin')
    def mutate(self, info, resource_id, **kwargs):
        validate_empty_fields(**kwargs)
        query = Resource.get_query(info)
        exact_resource = query.filter(ResourceModel.id == resource_id).first()

        if not exact_resource:
            raise GraphQLError("ResourceId not Found")

        update_entity_fields(exact_resource, **kwargs)
        exact_resource.save()
        return UpdateRoomResource(resource=exact_resource)


class DeleteResource(graphene.Mutation):

    class Arguments:
        resource_id = graphene.Int(required=True)
    resource = graphene.Field(Resource)

    @Auth.user_roles('Admin')
    def mutate(self, info, resource_id, **kwargs):
        query_room_resource = Resource.get_query(info)
        exact_room_resource = query_room_resource.filter(
            ResourceModel.id == resource_id).first()
        if not exact_room_resource:
            raise GraphQLError("Resource not found")

        exact_room_resource.delete()
        return DeleteResource(resource=exact_room_resource)


class Query(graphene.ObjectType):

    all_resources = graphene.Field(
        PaginatedResource,
        page=graphene.Int(),
        per_page=graphene.Int(),
        unique=graphene.Boolean())
    get_resources_by_room_id = graphene.List(lambda: Resource,
                                             room_id=graphene.Int())

    def resolve_all_resources(self, info, **kwargs):
        resp = PaginatedResource(**kwargs)
        return resp

    def resolve_get_resources_by_room_id(self, info, room_id):
        query = Resource.get_query(info)
        check_room = query.filter(ResourceModel.room_id == room_id).first()
        if not check_room:
            raise GraphQLError("Room has no resource yet")

        return query.filter(ResourceModel.room_id == room_id)


class Mutation(graphene.ObjectType):

    create_resource = CreateResource.Field()
    update_room_resource = UpdateRoomResource.Field()
    delete_resource = DeleteResource.Field()
