import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from helpers.auth.authentication import Auth
from api.structure.models import Structure as StructureModel


class Structure(SQLAlchemyObjectType):
    class Meta:
        model = StructureModel


class Query(graphene.ObjectType):
    all_structures = graphene.List(Structure)
    get_structure_by_web_id = \
      graphene.Field(Structure, web_id=graphene.String())

    @Auth.user_roles('Admin')
    def resolve_all_structures(self, info):
        query = Structure.get_query(info)
        return query.order_by(func.lower(StructureModel.name)).all()

    @Auth.user_roles('Admin')
    def resolve_get_structure_by_web_id(self, info, web_id):
        if not web_id.strip():
            raise GraphQLError("Please input a valid structure webId")
        query = Structure.get_query(info)
        structure = query.filter(StructureModel.web_id == web_id).first()
        if not structure:
            raise GraphQLError("Structure not found")
        return structure
