import graphene

import api.room.schema
import api.user.schema



class Query(
    api.room.schema.Query,
    api.user.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.user.schema.Mutation
):
    pass

admin_schema = graphene.Schema(query=Query, mutation=Mutation)