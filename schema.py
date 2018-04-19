import graphene

import api.room.schema


class Query(
    api.room.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
