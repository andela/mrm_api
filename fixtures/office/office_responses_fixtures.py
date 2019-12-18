from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None
get_office_by_name_response = {
    'data': {
        'getOfficeByName': [{
            'name': 'St. catherines',
            'id': '1',
            'blocks': [{
                'name': 'Ec',
                'floors': [{
                    'name': '3rd',
                    'id': '4',
                    'rooms': [{
                       'name': 'Entebbe',
                       'id': '1'}]
                }]
            }]
        }]
    }
}

omq_error = error_item
omq_error.message = "St. catherines Office already exists"
omq_error.locations = [{"line": 3, "column": 9}]
omq_error.path = ["createOffice"]
omq_data = {"createOffice": null}
office_mutation_query_duplicate_name_responce = build(
    omq_error.build_error(omq_error),
    omq_data
)

offices_query_response = {
    "data": {
        "allOffices": {
            "offices": [
                {
                    "name": "Dojo",
                    "id": "2"
                },
                {
                    "name": "Epic tower",
                    "id": "3"
                },
                {
                    "name": "St. catherines",
                    "id": "1"
                }
            ],
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

all_offices_query_response = {
    "data": {
        "allOffices": {
            "offices": [
                {
                    "name": "Dojo",
                    "id": "2"
                },
                {
                    "name": "Epic tower",
                    "id": "3"
                },
                {
                    "name": "St. catherines",
                    "id": "1"
                },
            ]
        }
    }
}

office_mutation_query_response = {'data': {'createOffice': {'office': {'name': 'The Crest', 'locationId': 1, 'blocks': [{'id': '3', 'name': 'The Crest'}]}}}}  # noqa
