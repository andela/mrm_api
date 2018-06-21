import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from api.floor.models import Floor as FloorModel


class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel


class Query(graphene.ObjectType):
    all_floors = graphene.List(Floor)
    get_rooms_in_a_floor = graphene.List(
        lambda: Floor,
        floor_id=graphene.Int()
    )

    def resolve_all_floors(self, info):
        query = Floor.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_floor(self, info, floor_id):
        query = Floor.get_query(info)
        result = query.filter(FloorModel.id == floor_id)
        return result
