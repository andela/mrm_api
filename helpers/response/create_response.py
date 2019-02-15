from datetime import datetime
from api.response.models import Response
from api.room_resource.models import Resource


def create_response(question_type, errors, responses, **kwargs):
    if question_type.lower() == 'rate':
        if 'rate' in kwargs and kwargs['rate']:
            rating = [1, 2, 3, 4, 5]
            if kwargs['rate'] not in rating:
                errors.append(
                    'Please rate between 1 and 5 for question {}'.format(
                        kwargs['question_id']))
                return responses, errors
            rating = Response(
                rate=kwargs['rate'],
                room_id=kwargs['room_id'],
                question_id=kwargs['question_id'],
                created_date=datetime.now())
            rating.save()
            responses.append(rating)
    if question_type.lower() == 'check':
        if 'missing_items' in kwargs and kwargs['missing_items']:
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
                    errors.append('Response to question {} was not saved because one of the resource provided does not exist'.format(kwargs['question_id'])) # noqa
                    return responses, errors
                response.missing_resources.append(
                    missing_item
                )
                response.save()
            responses.append(response)
    if question_type.lower() == 'input':
        if 'text_area' in kwargs and kwargs['text_area']:
            suggestion = Response(
                text_area=kwargs['text_area'],
                room_id=kwargs['room_id'],
                question_id=kwargs['question_id'],
                created_date=datetime.now())
            suggestion.save()
            responses.append(suggestion)
    return responses, errors
