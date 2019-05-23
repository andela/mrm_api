import os

import bugsnag
from flask_script import Manager, Shell
from flask_cors import CORS
from helpers.auth.allowed_requests import Request
from bugsnag.flask import handle_exceptions


# Configure bugnsag
bugsnag.configure(
    api_key=os.getenv('BUGSNAG_API_TOKEN'),
    release_stage="development",
    project_root="app"
)

# local imports
from app import create_app  # noqa: E402

app = create_app(os.getenv('APP_SETTINGS') or 'default')
with app.test_request_context():
    if app.config['DEBUG'] or app.config['TESTING']:
        CORS(app, resources={r"/mrm": {"origins": "*"}})
    else:
        Request.validate_origins()

handle_exceptions(app)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
