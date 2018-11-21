import graphene
import api.location.schema
import api.block.schema
import api.floor.schema
import api.room.schema
import api.room.schema_query
import api.room_resource.schema
import api.role.schema
import api.user.schema
import api.user_role.schema
import api.devices.schema
import api.office.schema
import api.wing.schema
import api.events.schema
import utilities.calendar_ids_cleanup
import api.notification.schema
import api.feedback.schema


class Query(
    api.location.schema.Query,
    api.block.schema.Query,
    api.floor.schema.Query,
    api.room.schema_query.Query,
    api.room_resource.schema.Query,
    api.role.schema.Query,
    api.user.schema.Query,
    api.user_role.schema.Query,
    api.devices.schema.Query,
    api.office.schema.Query,
    api.wing.schema.Query,
    utilities.calendar_ids_cleanup.Query,
    api.notification.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.room_resource.schema.Mutation,
    api.role.schema.Mutation,
    api.user.schema.Mutation,
    api.user_role.schema.Mutation,
    api.devices.schema.Mutation,
    api.location.schema.Mutation,
    api.office.schema.Mutation,
    api.events.schema.Mutation,
    api.notification.schema.Mutation,
    api.feedback.schema.Mutation,
    api.block.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
