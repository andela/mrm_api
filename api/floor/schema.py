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
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    floor = SQLAlchemyConnectionField(Floor)