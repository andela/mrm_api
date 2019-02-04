import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from graphql import GraphQLError

from api.room_resource.models import Resource as ResourceModel
from api.room.models import Room as RoomModel
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from helpers.pagination.paginate import Paginate, validate_page
from helpers.room_filter.room_filter import location_join_room


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
        active_resources = query.filter(ResourceModel.state == "active")
        if not page:
            if unique:
                return active_resources.distinct(ResourceModel.name).all()
            return active_resources.order_by(
                func.lower(ResourceModel.name)).all()
        page = validate_page(page)
        self.query_total = active_resources.count()
        result = active_resources.order_by(func.lower(
            ResourceModel.name)).limit(per_page).offset(page*per_page)
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
        location_query = location_join_room()
        room_location = location_query.filter(RoomModel.id == kwargs['room_id']).first()  # noqa: E501
        if not room_location:
            raise GraphQLError("Room not found")
        admin_roles.update_delete_rooms_create_resource(room_id=kwargs['room_id'])  # noqa: E501

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
        active_resources = query.filter(ResourceModel.state == "active")
        exact_resource = active_resources.filter(
            ResourceModel.id == resource_id).first()
        if not exact_resource:
            raise GraphQLError("Resource not found")

        admin_roles.update_resource(resource_id, room_id=kwargs['room_id'])

        update_entity_fields(exact_resource, **kwargs)
        exact_resource.save()
        return UpdateRoomResource(resource=exact_resource)


class DeleteResource(graphene.Mutation):

    class Arguments:
        resource_id = graphene.Int(required=True)
        state = graphene.String()
    resource = graphene.Field(Resource)

    @Auth.user_roles('Admin')
    def mutate(self, info, resource_id, **kwargs):
        query_room_resource = Resource.get_query(info)
        active_resources = query_room_resource.filter(
            ResourceModel.state == "active")
        exact_room_resource = active_resources.filter(
            ResourceModel.id == resource_id).first()
        if not exact_room_resource:
            raise GraphQLError("Resource not found")

        admin_roles.delete_resource(resource_id)
        update_entity_fields(exact_room_resource, state="archived", **kwargs)
        exact_room_resource.save()
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
        active_resources = query.filter(ResourceModel.state == "active")
        check_room = active_resources.filter(
            ResourceModel.room_id == room_id).first()
        if not check_room:
            raise GraphQLError("Room has no resource yet")

        return active_resources.filter(ResourceModel.room_id == room_id)


class Mutation(graphene.ObjectType):

    create_resource = CreateResource.Field()
    update_room_resource = UpdateRoomResource.Field()
    delete_resource = DeleteResource.Field()
