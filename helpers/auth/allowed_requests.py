import os
from flask import request, jsonify


def validate_origins():
    """validate requests for production environments"""

    user_agent = request.headers.get('User-Agent')
    if(os.getenv('APP_SETTINGS') == 'production'):
        if "insomnia" or "postman" in user_agent.lower():
            return jsonify(
                {
                    'message':
                    'Invalid request. You are not allowed to make requests to this environment'  # noqa 501
                }), 401
