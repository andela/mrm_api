import itertools

import graphene
from math import ceil
from graphql import GraphQLError


class Paginate(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()

    def __init__(self, **kwargs):
        self.page = kwargs.pop('page', None)
        self.per_page = kwargs.pop('per_page', None)
        self.unique = kwargs.pop('unique', None)
        self.query_total
        self.pages
        self.filter_data = {}
        self.filter_data.update(**kwargs)

    def resolve_pages(self, pages):
        if self.per_page:
            self.pages = ceil(self.query_total / self.per_page)
        pages = self.pages
        return pages

    def resolve_has_next(self, has_next):
        if self.page:
            page = self.page
            pages = self.pages
            pages = self.resolve_pages(pages)
            if page < pages:
                has_next = True
            else:
                has_next = False
        return has_next

    def resolve_has_previous(self, has_previous):
        if self.page:
            page = self.page
            pages = self.resolve_pages(self.pages)
            if (page > 1) and (pages > 1) and (page <= pages):
                has_previous = True
            else:
                has_previous = False

        return has_previous


def validate_page(page):
    if page < 1:
        raise GraphQLError("No page requested")
    else:
        return page - 1


class ListPaginate:
    """Handles pagination for data(list) which is queried from google calendar
    API rather than from our database
    """
    def __init__(self, iterable, per_page, page):
        self.iterable = iterable
        self.per_page = per_page
        self.page = page
        self.query_total = self.get_query_total()
        self.pages = self.get_pages()
        self.has_next = self.get_has_next()
        self.has_previous = self.get_has_previous()
        self.paginated = self.get_paginated()
        self.current_page = self.get_current_page()

    def get_query_total(self):
        return len(self.iterable)

    def get_pages(self):
        pages = ceil(self.query_total / self.per_page)
        return pages

    def get_has_next(self):
        if self.page < self.pages:
            has_next = True
        else:
            has_next = False
        return has_next

    def get_has_previous(self):
        if self.page > 1:
            has_previous = True
        else:
            has_previous = False
        return has_previous

    @staticmethod
    def get_paginated_result(iterable, per_page):
        while True:
            it1, it2 = itertools.tee(iterable)
            iterable, result = (itertools.islice(it1, per_page, None),
                                list(itertools.islice(it2, per_page)))
            if len(result) == 0:
                break
            yield result

    # get page_number that can be used in list indexing
    def get_page_index(self):
        if self.page < 1:
            raise GraphQLError("Invalid page requested")
        return self.page - 1

    def get_paginated(self):
        result = self.get_paginated_result(
            iterable=self.iterable, per_page=self.per_page)
        return list(result)

    def get_current_page(self):
        try:
            self.current_page = self.paginated[self.get_page_index()]
        except IndexError:
            raise GraphQLError("Page does not exist")
        return self.current_page
