null = None

create_feedback_query = '''
mutation {
    createFeedback(roomId:1, overallRating:"Good", cleanlinessRating:"Excellent", comments:"lock not working") {  # noqa
        feedback{
            roomId
            overallRating
            cleanlinessRating
            comments
        }
    }
}
'''

create_feedback_response = {
    "data": {
        "createFeedback": {
            "feedback": {
                "roomId": 1,
                "overallRating": "Good",
                "cleanlinessRating": "Excellent",
                "comments": "lock not working"
            }
        }
    }
}

create_feedback_with_no_rating_or_comment_query = '''
mutation {
    createFeedback(roomId:1) {
        feedback{
            roomId
            overallRating
            cleanlinessRating
            comments
        }
    }
}
'''

create_feedback_with_no_rating_or_comment_response = {
    "errors": [
        {
            "message": "Ensure to give at least one feedback input",
            "locations": [
                {
                    "line": 3,
                    "column": 5
                }
            ],
            "path": [
                "createFeedback"
            ]
        }
    ],
    "data": {
        "createFeedback": null
    }
}

create_feedback_with_invalid_rating_query = '''
mutation {
    createFeedback(roomId:1, overallRating:"Invalid rating") {
        feedback{
            roomId
            overallRating
            cleanlinessRating
            comments
        }
    }
}
'''

create_feedback_with_invalid_rating_response = {
    "errors": [
        {
            "message": "Invalid rating, only Excellent, Very Good, Good, Average, Poor ratings allowed",  # noqa
            "locations": [
                {
                    "line": 3,
                    "column": 5
                }
            ],
            "path": [
                "createFeedback"
            ]
        }
    ],
    "data": {
        "createFeedback": null
    }
}

create_feedback_with_non_existent_room_id_query = '''
mutation {
    createFeedback(roomId:199, overallRating:"Good") {  # noqa
        feedback{
            roomId
            overallRating
            cleanlinessRating
            comments
        }
    }
}
'''

create_feedback_with_non_existent_room_id_response = {
    "errors": [
        {
            "message": "Non-existent room id",
            "locations": [
                {
                    "line": 3,
                    "column": 5
                }
            ],
            "path": [
                "createFeedback"
            ]
        }
    ],
    "data": {
        "createFeedback": null
    }
}
