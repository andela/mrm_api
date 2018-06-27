import graphene
import api.location.schema
import api.block.schema
import api.floor.schema
import api.room.schema
import api.room_resource.schema
import api.office.schema


class Query(
    api.location.schema.Query,
    api.block.schema.Query,
    api.floor.schema.Query,
    api.room.schema.Query,
    api.room_resource.schema.Query

):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.room_resource.schema.Mutation,
    api.office.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
