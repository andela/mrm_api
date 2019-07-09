from datetime import datetime
from api.response.models import Response
from api.room_resource.models import Resource as ResourceModel
from api.room.models import RoomResource
from api.room_resource.schema import Resource
from api.question.schema_query import Question
import graphene


class Rate(graphene.ObjectType):
    rate = graphene.Int()


class SelectedOptions(graphene.ObjectType):
    options = graphene.List(graphene.String)


class TextArea(graphene.ObjectType):
    suggestion = graphene.String()


class MissingItems(graphene.ObjectType):
    missing_items = graphene.List(Resource)


def map_response_type(question_type):
    return {
            'check': lambda check_options: SelectedOptions(
                options=check_options
            ),
            'textarea': lambda suggestion: TextArea(suggestion=suggestion[0]),
            'missingitem': lambda missing_items: MissingItems(
                missing_items=map(lambda id: ResourceModel.query.filter_by(
                    id=id  # map each resource id and return the corresponding resource # noqa
            ).first(), missing_items)),
            'rate': lambda rate: Rate(rate=rate[0])
        }.get(question_type)


def create_response(info, question_type, errors, responses, **kwargs): # noqa
    if question_type.lower() == 'rate' and \
            'rate' in kwargs and kwargs['rate']:
        rating = [1, 2, 3, 4, 5]
        if kwargs['rate'] not in rating:
            errors.append(
                'Please rate between 1 and 5 for question {}'.format(
                    kwargs['question_id']))
            return responses, errors
        rating = Response(
            response=[kwargs['rate']],
            question_type="rate",
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        rating.save()
        rating.response = map_response_type(question_type)(rating.response)
        responses.append(rating)
    elif question_type.lower() == 'check' and 'selected_options' in kwargs:
        question = Question.get_query(info).filter_by(
            id=kwargs['question_id']
        ).first()
        for option in kwargs['selected_options']:
            if option not in question.check_options:
                errors.append(
                    'Invalid option {} selected. Check options are {}'
                    .format(option, question.check_options)
                )
                return responses, errors
        response = Response(
            response=kwargs['selected_options'],
            question_type="check",
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        response.save()
        response.response = map_response_type(question_type)(response.response)
        responses.append(response)
    elif question_type.lower() == 'missingitem' and 'missing_items' in kwargs\
            and kwargs['missing_items']:
        response = Response(
            response=set(kwargs['missing_items']),  # save unique ids
            room_id=kwargs['room_id'],
            question_type="missingitem",
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        response.save()
        for item_id in set(kwargs['missing_items']):
            missing_item = None
            room_missing_item = RoomResource.query.filter_by(
                resource_id=item_id, room_id=kwargs['room_id']).first()
            if room_missing_item:
                missing_item = ResourceModel.query.filter_by(
                    id=item_id).first()
            if missing_item is None:
                response.delete()
                errors.append(
                    'Response to question {} was not saved because one of the resources provided was not assigned to the room' # noqa
                    .format(kwargs['question_id'])
                )
                return responses, errors
            response.missing_resources.append(
                missing_item
            )
            response.save()
        response.response = map_response_type(question_type)(
            missing_items=[
                resource.id for resource in response.missing_resources
            ]
        )
        responses.append(response)
    elif question_type.lower() == 'input' and \
            'text_area' in kwargs and kwargs['text_area']:
        suggestion = Response(
            response=[kwargs['text_area']],
            question_type="textarea",
            room_id=kwargs['room_id'],
            question_id=kwargs['question_id'],
            created_date=datetime.now())
        suggestion.save()
        suggestion.response = map_response_type('textarea')(
            suggestion=suggestion.response
        )
        responses.append(suggestion)
    else:
        errors.append("Kindly respond to the right question type of {}".format(question_type))  # noqa
    return responses, errors
