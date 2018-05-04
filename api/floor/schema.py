import graphene
from graphene import relay

from graphene_sqlalchemy import(
    SQLAlchemyConnectionField,
    SQLAlchemyObjectType
)

from api.floor.models import Floor as FloorModel

class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    floor = graphene.List(Floor)

    def resolve_floors(self,info):
        query = Floor.get_query(info)
        return query.all()
