import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.office.models import Office as OfficeModel
from api.location.models import Location
from helpers.auth.authentication import Auth
from helpers.room_filter.room_filter import room_join_location, lagos_office_join_location  # noqa: E501
from helpers.auth.admin_roles import admin_roles


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
            exact_query = room_join_location(query)
            result = exact_query.filter(OfficeModel.name == name)
            return result.all()


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
