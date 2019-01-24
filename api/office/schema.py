import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from sqlalchemy import exc, func

from api.office.models import Office as OfficeModel
from api.location.models import Location
from utilities.validations import update_entity_fields, validate_empty_fields
from helpers.auth.authentication import Auth
from helpers.room_filter.room_filter import room_join_location, lagos_office_join_location  # noqa: E501
from helpers.auth.admin_roles import admin_roles
from helpers.auth.error_handler import SaveContextManager
from helpers.pagination.paginate import Paginate, validate_page
from helpers.email.email import office_created


class Office(SQLAlchemyObjectType):
    class Meta:
        model = OfficeModel


class CreateOffice(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        location_id = graphene.Int(required=True)

    office = graphene.Field(Office)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        location = Location.query.filter_by(id=kwargs['location_id']).first()
        if not location:
            raise GraphQLError("Location not found")
        admin_roles.create_office(location_id=kwargs['location_id'])
        office = OfficeModel(**kwargs)
        with SaveContextManager(office, kwargs['name'], 'Office'):
            new_office = kwargs['name']
            if not office_created(new_office):
                raise GraphQLError("Office created but Emails not Sent")
            return CreateOffice(office=office)


class DeleteOffice(graphene.Mutation):
    class Arguments:
        office_id = graphene.Int(required=True)

    office = graphene.Field(Office)

    @Auth.user_roles('Admin')
    def mutate(self, info, office_id, **kwargs):
        query_office = Office.get_query(info)
        exact_office = query_office.filter(
            OfficeModel.id == office_id).first()  # noqa: E501
        if not exact_office:
            raise GraphQLError("Office not found")

        admin_roles.create_rooms_update_delete_office(office_id)
        exact_office.delete()
        return DeleteOffice(office=exact_office)


class UpdateOffice(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        office_id = graphene.Int()

    office = graphene.Field(Office)

    @Auth.user_roles('Admin')
    def mutate(self, info, office_id, **kwargs):
        validate_empty_fields(**kwargs)
        get_office = Office.get_query(info)
        exact_office = get_office.filter(OfficeModel.id == office_id).first()
        if not exact_office:
            raise GraphQLError("Office not found")
        admin_roles.create_rooms_update_delete_office(office_id)
        try:
            update_entity_fields(exact_office, **kwargs)
            exact_office.save()
        except exc.SQLAlchemyError:
            raise GraphQLError("Action Failed")

        return UpdateOffice(office=exact_office)


class PaginateOffices(Paginate):
    offices = graphene.List(Office)

    def resolve_offices(self, info, **kwargs):
        page = self.page
        per_page = self.per_page
        query = Office.get_query(info)
        if not page:
            return query.order_by(func.lower(OfficeModel.name)).all()
        page = validate_page(page)
        self.query_total = query.count()
        result = query.order_by(
            func.lower(OfficeModel.name)).limit(
            per_page).offset(page * per_page)
        if result.count() == 0:
            return GraphQLError("No more offices")
        return result


class Query(graphene.ObjectType):
    get_office_by_name = graphene.List(Office, name=graphene.String())
    all_offices = graphene.Field(
        PaginateOffices, page=graphene.Int(), per_page=graphene.Int())

    def resolve_all_offices(self, info, **kwargs):
        response = PaginateOffices(**kwargs)
        return response

    def resolve_get_office_by_name(self, info, name):
        query = Office.get_query(info)
        check_office = query.filter(OfficeModel.name == name).first()
        if not check_office:
            raise GraphQLError("Office Not found")

        if name == "Epic tower":
            exact_query = lagos_office_join_location(query)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()

        else:
            exact_query = room_join_location(query)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
    delete_office = DeleteOffice.Field()
    update_office = UpdateOffice.Field()
