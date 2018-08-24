import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.office.models import Office as OfficeModel
from api.location.models import Location as LocationModel
from api.location.schema import Location
from helpers.auth.authentication import Auth
from helpers.room_filter.room_filter import office_join_location, lagos_office_join_location  # noqa: E501
from helpers.auth.user_details import get_user_from_db


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
        query = Location.get_query(info)
        location = query.filter(
            LocationModel.id == kwargs['location_id']).first()
        admin_details = get_user_from_db()
        if location.name != admin_details.location:
            raise GraphQLError("You cannot make changes outside your location")
        office = OfficeModel(**kwargs)
        office.save()
        return CreateOffice(office=office)


class Query(graphene.ObjectType):
    get_office_by_name = graphene.List(
        Office,
        name=graphene.String()
    )

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
            exact_query = office_join_location(query)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
