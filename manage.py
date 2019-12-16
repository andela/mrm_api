import os

import bugsnag
import logging
from flask_script import Manager, Shell
from bugsnag.flask import handle_exceptions
from bugsnag.handlers import BugsnagHandler
from bugsnag.celery import connect_failure_handler

connect_failure_handler()

# Configure bugnsag
bugsnag.configure(
    api_key=os.getenv('BUGSNAG_API_TOKEN'),
    release_stage="development",
    asynchronous=False,
    auto_capture_sessions=True,
    notify_release_stages=['development', 'production']
)
logger = logging.getLogger("test.logger")
handler = BugsnagHandler()

# send only ERROR-level logs and above
handler.setLevel(logging.ERROR)
logger.addHandler(handler)

# local imports
from app import create_app  # noqa: E402

app = create_app(os.getenv('APP_SETTINGS') or 'default')
handle_exceptions(app)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
