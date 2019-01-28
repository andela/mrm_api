import graphene
from sqlalchemy import func
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.tag.models import Tag as TagModel
from utilities.validations import validate_empty_fields
from helpers.auth.authentication import Auth
from helpers.auth.validator import ErrorHandler


class Tag(SQLAlchemyObjectType):
    class Meta:
        model = TagModel


class CreateTag(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        color = graphene.String(required=True)
        description = graphene.String(required=True)
        room_tags = graphene.List(graphene.Int)
    tag = graphene.Field(Tag)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        tag = TagModel(**kwargs)
        query = Tag.get_query(info)
        tags = query.filter(
            func.lower(TagModel.name) == func.lower(kwargs.get('name')))
        if tags.count():
            ErrorHandler.check_conflict(self, kwargs['name'], 'Tag')
        tag.save()
        return CreateTag(tag=tag)


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
