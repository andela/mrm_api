all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id': '1',
                'questionType': 'rate',
                'questionTitle': 'Rating Feedback',
                'question': 'How will you rate the brightness of the room',
                'startDate': '20 Nov 2018',
                'endDate': '28 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                {
                'id': '2',
                'questionType': 'check',
                'questionTitle': 'check Feedback',
                'question':  'Is there anything missing in the room',
                'startDate': '20 Nov 2018',
                'endDate': '30 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '2',
                    'questionId': 2,
                    'roomId': 1
                }]
            },
                {
                'id': '3',
                'questionType': 'input',
                'questionTitle': 'input Feedback',
                'question': 'Any other suggestion',
                'startDate': '20 Nov 2018',
                'endDate': '28 Nov 2018',
                'questionResponseCount': 0,
                'response': []
            },
                {
                'id': '4',
                'questionType': 'check',
                'questionTitle': 'Missing item',
                'question':  'Anything missing in the room?',
                'startDate': '20 Nov 2018',
                'endDate': '30 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '3',
                    'questionId': 4,
                    'roomId': 2
                }]
            }]
        }
    }
}

paginated_all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id':
                '1',
                'questionType':
                'rate',
                'question':
                'How will you rate the brightness of the room',
                'startDate':
                '20 Nov 2018',
                'endDate':
                '28 Nov 2018',
                'questionResponseCount':
                1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                {
                'id': '2',
                'questionType': 'check',
                'question':
                'Is there anything missing in the room',
                'startDate': '20 Nov 2018',
                'endDate': '30 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '2',
                    'questionId': 2,
                    'roomId': 1
                }]
            }]
        }
    }
}

get_question_by_id_query_response = {
    'data': {
        'question': {
            'id': '1',
            'questionType': 'rate',
            'question': 'How will you rate the brightness of the room',
            'startDate': '20 Nov 2018',
            'endDate': '28 Nov 2018',
            'questionResponseCount': 1,
            'response': [{
                'id': '1',
                'questionId': 1,
                'roomId': 1
            }]
        }
    }
}

get_all_questions_query_response = {
    "data": {
        "allQuestions": [
            {
                "questionType": "rate"
            },
            {
                "questionType": "input"
            }
        ]
    }
}

all_questions_query_no_date_range_response = {
    "data": {
        "allQuestions": [
            {
                "questionType": "rate"
            },
            {
                "questionType": "check"
            },
            {
                "questionType": "input"
            },
            {
                "questionType": "check"
            }
        ]
    }
}
