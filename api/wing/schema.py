import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.floor.models import Floor
from api.wing.models import Wing as WingModel
from utilities.utility import update_entity_fields, validate_empty_fields
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager
from helpers.auth.admin_roles import admin_roles
from helpers.pagination.paginate import Paginate, validate_page


class Wing(SQLAlchemyObjectType):
    class Meta:
        model = WingModel


class CreateWing(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        floor_id = graphene.Int(required=True)

    wing = graphene.Field(Wing)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        floor = Floor.query.filter_by(id=kwargs['floor_id']).first()
        if not floor:
            raise GraphQLError("Floor not found")
        admin_roles.check_office_location_create_wing(floor_id=kwargs['floor_id'])  # noqa: E501
        admin_roles.create_update_delete_wing()
        wing = WingModel(**kwargs)
        with SaveContextManager(wing, kwargs['name'], 'Wing'):
            return CreateWing(wing=wing)


class DeleteWing(graphene.Mutation):
    class Arguments:
        wing_id = graphene.Int(required=True)

    wing = graphene.Field(Wing)

    @Auth.user_roles('Admin')
    def mutate(self, info, wing_id, **kwargs):
        query_wing = Wing.get_query(info)
        exact_wing = query_wing.filter(
            WingModel.id == wing_id).first()
        if not exact_wing:
            raise GraphQLError("Wing not found")
        admin_roles.create_update_delete_wing()
        exact_wing.delete()
        return DeleteWing(wing=exact_wing)


class UpdateWing(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        wing_id = graphene.Int()

    wing = graphene.Field(Wing)

    @Auth.user_roles('Admin')
    def mutate(self, info, wing_id, **kwargs):
        validate_empty_fields(**kwargs)
        get_wing = Wing.get_query(info)
        exact_wing = get_wing.filter(WingModel.id == wing_id).first()
        if not exact_wing:
            raise GraphQLError("Wing not found")
        admin_roles.create_update_delete_wing()
        update_entity_fields(exact_wing, **kwargs)
        with SaveContextManager(exact_wing, kwargs['name'], 'Wing'):
            return UpdateWing(wing=exact_wing)


class PaginatedWings(Paginate):
    wings = graphene.List(Wing)

    def resolve_wings(self, info, **kwargs):
        ''' This function paginates the returned response
        if page parameter is passed,
        otherwise it returns all floors
        '''
        page = self.page
        per_page = self.per_page
        query = Wing.get_query(info)
        if not page:
            return query.all()
        page = validate_page(page)
        self.query_total = query.count()
        result = query.limit(per_page).offset(page*per_page)
        if result.count() == 0:
            raise GraphQLError("No more wings")
        return result


class Query(graphene.ObjectType):
    all_wings = graphene.Field(
        PaginatedWings,
        page=graphene.Int(),
        per_page=graphene.Int(),
    )

    def resolve_all_wings(self, info, **kwargs):
        response = PaginatedWings(**kwargs)
        return response


class Mutation(graphene.ObjectType):
    create_wing = CreateWing.Field()
    delete_wing = DeleteWing.Field()
    update_wing = UpdateWing.Field()
