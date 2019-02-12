import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from sqlalchemy import exc, func

from api.office.models import Office as OfficeModel
from api.location.models import Location
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.room_filter.room_filter import (
    room_join_location,
    lagos_office_join_location)
from helpers.auth.admin_roles import admin_roles
from helpers.auth.error_handler import SaveContextManager
from helpers.pagination.paginate import Paginate, validate_page
from helpers.email.email import send_email_notification
from helpers.auth.user_details import get_user_from_db


class Office(SQLAlchemyObjectType):
    class Meta:
        model = OfficeModel


class CreateOffice(graphene.Mutation):
    class Arguments:
        state = graphene.String()
        name = graphene.String(required=True)
        location_id = graphene.Int(required=True)

    office = graphene.Field(Office)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        location = Location.query.filter_by(id=kwargs['location_id']).first()
        if not location:
            raise GraphQLError("Location not found")
        admin_roles.verify_admin_location(location_id=kwargs['location_id'])
        office = OfficeModel(**kwargs)
        admin = get_user_from_db()
        email = admin.email
        payload = {
            'model': OfficeModel, 'field': 'name', 'value':  kwargs['name']
            }
        with SaveContextManager(
           office, 'Office', payload
        ):
            new_office = kwargs['name']
            if not send_email_notification(email, new_office, location.name):
                raise GraphQLError("Office created but Emails not Sent")
            return CreateOffice(office=office)


class DeleteOffice(graphene.Mutation):
    class Arguments:
        office_id = graphene.Int(required=True)
        state = graphene.String()

    office = graphene.Field(Office)

    @Auth.user_roles('Admin')
    def mutate(self, info, office_id, **kwargs):
        query_office = Office.get_query(info)
        result = query_office.filter(OfficeModel.state == "active")
        exact_office = result.filter(
            OfficeModel.id == office_id).first()  # noqa: E501
        if not exact_office:
            raise GraphQLError("Office not found")

        admin_roles.create_rooms_update_delete_office(office_id)
        update_entity_fields(exact_office, state="archived", **kwargs)
        exact_office.save()
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
        result = get_office.filter(OfficeModel.state == "active")
        exact_office = result.filter(OfficeModel.id == office_id).first()
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
        active_offices = query.filter(OfficeModel.state == "active")
        if not page:
            return active_offices.order_by(func.lower(OfficeModel.name)).all()
        page = validate_page(page)
        self.query_total = active_offices.count()
        result = active_offices.order_by(
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
        active_offices = query.filter(OfficeModel.state == "active")
        check_office = active_offices.filter(OfficeModel.name == name).first()
        if not check_office:
            raise GraphQLError("Office Not found")
        if name == "Epic tower":
            exact_query = lagos_office_join_location(active_offices)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()
        else:
            exact_query = room_join_location(active_offices)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
    delete_office = DeleteOffice.Field()
    update_office = UpdateOffice.Field()
