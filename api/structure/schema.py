import graphene
from graphql import GraphQLError
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from api.structure.models import Structure as StructureModel

class Structure(SQLAlchemyObjectType):
    class Meta:
        model = StructureModel


class Query(graphene.ObjectType):
    all_structures = graphene.List(Structure)
    get_structure_by_web_id = graphene.Field(Structure, web_id=graphene.String())

    def resolve_all_structures(self, info):
        query = Structure.get_query(info)
        return query.order_by(func.lower(StructureModel.name)).all()


