import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.office.models import Office as OfficeModel
from helpers.auth.authentication import Auth


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
        office = OfficeModel(**kwargs)
        office.save()
        return CreateOffice(office=office)


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
