import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from api.office.models import Office as OfficeModel


class Office(SQLAlchemyObjectType):
    class Meta:
        model = OfficeModel


class Query(graphene.ObjectType):
    all_offices = graphene.List(Office)
    get_rooms_in_an_office = graphene.List(
        lambda: Office,
        office_id=graphene.Int()
    )

    def resolve_all_offices(self, info):
        query = Office.get_query(info)
        return query.all()

    def resolve_get_rooms_in_an_office(self, info, office_id):
        query = Office.get_query(info)
        result = query.filter(OfficeModel.id == office_id)
        return result
