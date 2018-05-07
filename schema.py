import graphene
import api.location.schema
import api.block.schema
import api.floor.schema
import api.room.schema
import api.equipment.schema


class Query(
    api.location.schema.Query,
    api.block.schema.Query,
    api.floor.schema.Query,
    api.room.schema.Query,
    api.equipment.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.equipment.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
