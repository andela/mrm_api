import graphene
from sqlalchemy import func
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.tag.models import Tag as TagModel
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
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


class UpdateTag(graphene.Mutation):
    class Arguments:
        tag_id = graphene.Int(required=True)
        name = graphene.String()
        color = graphene.String()
        description = graphene.String()
    tag = graphene.Field(Tag)

    @Auth.user_roles('Admin')
    def mutate(self, info, tag_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_tag = Tag.get_query(info)
        tag = query_tag.filter(
            TagModel.id == tag_id).first()
        if not tag:
            raise GraphQLError("Tag not found")
        update_entity_fields(tag, **kwargs)
        tag.save()
        return UpdateTag(tag=tag)


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    update_tag = UpdateTag.Field()
