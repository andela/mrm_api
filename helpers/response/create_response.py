from datetime import datetime
from api.response.models import Response
from api.room_resource.models import Resource
from api.room.models import RoomResource


def create_response(question_type, errors, responses, **kwargs):
    if question_type.lower() == 'rate' and 'rate' in kwargs and kwargs['rate']: # noqa
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
    elif question_type.lower() == 'check' and 'missing_items' in kwargs and kwargs['missing_items']: # noqa
        response = Response(
            check=True,
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        response.save()
        for item_id in kwargs['missing_items']:
            missing_item = None
            room_missing_item = RoomResource.query.filter_by(
                resource_id=item_id, room_id=kwargs['room_id']).first()
            if room_missing_item:
                missing_item = Resource.query.filter_by(
                    id=item_id).first()
            if missing_item is None:
                response.delete()
                errors.append('Response to question {} was not saved because one of the resources provided was not assigned to the room'.format(kwargs['question_id'])) # noqa
                return responses, errors
            response.missing_resources.append(
                missing_item
            )
            response.save()
            responses.append(response)
    elif question_type.lower() == 'input' and 'text_area' in kwargs and kwargs['text_area']: # noqa
        suggestion = Response(
            text_area=kwargs['text_area'],
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        suggestion.save()
        responses.append(suggestion)
    else:
        errors.append("Kindly respond to the right question type of {}".format(question_type)) # noqa
    return responses, errors
