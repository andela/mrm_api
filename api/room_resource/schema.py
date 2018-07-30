import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphql import GraphQLError

from api.room_resource.models import Resource as ResourceModel
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.authentication import Auth


class Resource(SQLAlchemyObjectType):

    class Meta:
        model = ResourceModel

class PaginatedResource(graphene.ObjectType):
    pages = graphene.Int()
    limit = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    resources = graphene.List(Resource)
    


# def PaginatedResource(**kwargs):
#     print("page info is", kwargs)
#     return kwargs


class PaginatedResource(graphene.ObjectType):
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    resources = graphene.List(Resource)
    
    def resolve_resources(self, info, **kwargs):
        print("this is kwargs", kwargs)
        page = kwargs.pop("page")
        per_page = kwargs.pop("per_page")
        if page < 1:
            return GraphQLError("No page requested")
        page = page - 1

        query = Resource.get_query(info)
        print("this is query", query)
        result = query.limit(per_page).offset(page*per_page)
        # import pdb; pdb.set_trace()
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
    
    all_resources = graphene.Field(PaginatedResource, page=graphene.Int(),
                            per_page=graphene.Int())
    get_resources_by_room_id = graphene.List(lambda: Resource,
                                             room_id=graphene.Int())

    def resolve_all_resources(self, info, **kwargs):
        print("the kwargs are:", kwargs)
        resp = PaginatedResource(kwargs)
        return resp        

    
    def resolve_get_resources_by_room_id(self, info, room_id):
        query = Resource.get_query(info)
        check_room = query.filter(ResourceModel.room_id == room_id).first()
        if not check_room:
            raise GraphQLError("Room has no resource yet")

        return query.filter(ResourceModel.room_id == room_id)      

    
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
