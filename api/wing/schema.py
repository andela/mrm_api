import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)

from api.wing.models import Wing as WingModel


class Wing(SQLAlchemyObjectType):
    class Meta:
        model = WingModel


class Query(graphene.ObjectType):
    all_wings = graphene.List(Wing)

    def resolve_all_wings(self, info):
        query = Wing.get_query(info)
        return query.all()
