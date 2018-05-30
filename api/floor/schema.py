import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.floor.models import Floor as FloorModel


class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel


class Query(graphene.ObjectType):
    floor = graphene.List(Floor)

    def resolve_floors(self, info):
        query = Floor.get_query(info)
        return query.all()
