import graphene
from graphene_sqlalchemy import (SQLAlchemyObjectType)
from api.office.models import Office as OfficeModel


class Office(SQLAlchemyObjectType):

    class Meta:
        model = OfficeModel


class CreateOffice(graphene.Mutation):

    class Arguments:
        building_name = graphene.String(required=True)
        location_id = graphene.Int(required=True)
    office = graphene.Field(Office)

    def mutate(self, info, **kwargs):
        office = OfficeModel(**kwargs)
        office.save()

        return CreateOffice(office=office)


class Mutation(graphene.ObjectType):
    create_office = CreateOffice.Field()
