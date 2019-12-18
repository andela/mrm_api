from .questions_fixtures_helper import (
    start_date, end_date
)

create_question_response = {
    "data": {
        "createQuestion": {
            "question": {
                "id": "5",
                "question": "How will you rate the cleanliness of the room",
                "questionType": "rate",
                "startDate": start_date.replace('T', ' '),
                "endDate": end_date.replace('T', ' ')
            }
        }
    }
}

update_question_response = {
    "data": {
        "updateQuestion": {
            "question": {
                "id": "1",
                "startDate": start_date.replace('T', ' '),
                "endDate": end_date.replace('T', ' '),
            }
        }
    }
}

delete_question_response = {
    "data": {
        "deleteQuestion": {
            "question": {
                "id": "1"
            }
        }
    }
}

all_questions_response = {
    "data": {
        "allQuestions": [
            {
                "question": "How will you rate the brightness of the room",
                "id": "1",
                "questionType": "rate"
            },
            {
                'question': 'Is there anything missing in the room',
                'id': '2',
                'questionType': 'check'
            },
            {
                'question': 'Any other suggestion',
                'id': '3',
                'questionType': 'input'
            },
            {
                'question': 'Anything missing in the room?',
                'id': '4',
                'questionType': 'check'
            }
        ]
    }
}
