import graphene
import api.location.schema
import api.room.schema
import api.room.schema_query
import api.room_resource.schema
import api.role.schema
import api.user.schema
import api.devices.schema
import api.events.schema
import utilities.calendar_ids_cleanup
import api.notification.schema
import api.question.schema
import api.response.schema
import api.response.schema_query
import api.tag.schema
import api.response.schema_query
import api.structure.schema
import api.analytics.all_analytics_query


class Query(
        api.location.schema.Query,
        api.room.schema_query.Query,
        api.room_resource.schema.Query,
        api.role.schema.Query,
        api.user.schema.Query,
        api.devices.schema.Query,
        utilities.calendar_ids_cleanup.Query,
        api.notification.schema.Query,
        api.response.schema.Query,
        api.response.schema_query.Query,
        api.question.schema.Query,
        api.structure.schema.Query,
        api.analytics.all_analytics_query.Query,
        api.events.schema.Query,
):
    """Root for converge Graphql queries"""
    pass


class Mutation(
        api.room.schema.Mutation,
        api.room_resource.schema.Mutation,
        api.role.schema.Mutation,
        api.user.schema.Mutation,
        api.devices.schema.Mutation,
        api.location.schema.Mutation,
        api.events.schema.Mutation,
        api.notification.schema.Mutation,
        api.question.schema.Mutation,
        api.response.schema.Mutation,
        api.tag.schema.Mutation,
        api.structure.schema.Mutation,
):
    """The root query for implementing GraphQL mutations."""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
