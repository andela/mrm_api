from datetime import datetime
from graphql import GraphQLError
from api.response.models import Response
from api.room_resource.models import Resource
from utilities.validations import (
    validate_rating_field,
    validate_missing_items_field)


def create_response(question_type, **kwargs):
    if question_type.lower() == 'rate':
        if 'rate' not in kwargs:
            raise GraphQLError("Provide a rating response")
        else:
            validate_rating_field(**kwargs)
            rating = Response(
                rate=kwargs['rate'],
                room_id=kwargs['room_id'],
                question_id=kwargs['question_id'],
                created_date=datetime.now())
            rating.save()
            return rating
    if question_type.lower() == 'check':
        validate_missing_items_field(**kwargs)
        response = Response(
            check=True,
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        response.save()
        for item_id in kwargs['missing_items']:
            missing_item = Resource.query.filter_by(
                id=item_id, room_id=kwargs['room_id']).first()
            if not missing_item:
                response.delete()
                raise GraphQLError(
                    'One of the resource provided does not exist in this room')
            response.missing_resources.append(
                missing_item
            )
            response.save()
        return response
    if question_type.lower() == 'input':
        if 'text_area' not in kwargs:
            raise GraphQLError("Provide a text response")
        suggestion = Response(
            text_area=kwargs['text_area'],
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        suggestion.save()
        return suggestion
