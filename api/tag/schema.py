import graphene
from sqlalchemy import exc, func
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.tag.models import Tag as TagModel
from utilities.validator import ErrorHandler
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager


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
        try:
            validate_empty_fields(**kwargs)
            tag = TagModel(**kwargs)
            payload = {
                'model': TagModel, 'field': 'name', 'value':  kwargs['name']
                }
            query = Tag.get_query(info)
            result = query.filter(TagModel.state == "active")
            tag_name = result.filter(
                func.lower(TagModel.name) ==
                func.lower(kwargs['name'])).count()
            if tag_name > 0:
                ErrorHandler.check_conflict(self, kwargs['name'], 'Tag')
            with SaveContextManager(tag, 'Tag', payload):
                return CreateTag(tag=tag)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class UpdateTag(graphene.Mutation):
    class Arguments:
        tag_id = graphene.Int(required=True)
        name = graphene.String()
        color = graphene.String()
        description = graphene.String()
    tag = graphene.Field(Tag)

    @Auth.user_roles('Admin')
    def mutate(self, info, tag_id, **kwargs):
        try:
            validate_empty_fields(**kwargs)
            query_tag = Tag.get_query(info)
            tag = query_tag.filter(
                TagModel.id == tag_id).first()
            if not tag:
                raise GraphQLError("Tag not found")
            update_entity_fields(tag, **kwargs)
            tag.save()
            return UpdateTag(tag=tag)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class DeleteTag(graphene.Mutation):
    class Arguments:
        tag_id = graphene.Int(required=True)
        state = graphene.String()
    tag = graphene.Field(Tag)

    @Auth.user_roles('Admin')
    def mutate(self, info, tag_id, **kwargs):
        try:
            query = Tag.get_query(info)
            result = query.filter(TagModel.state == "active")
            tag = result.filter(
                TagModel.id == tag_id).first()
            if not tag:
                raise GraphQLError("Tag not found")
            update_entity_fields(tag, state="archived", **kwargs)
            tag.save()
            return DeleteTag(tag=tag)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    update_tag = UpdateTag.Field()
    delete_tag = DeleteTag.Field()
