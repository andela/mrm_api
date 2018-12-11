import os

import bugsnag
import eventlet; eventlet.monkey_patch(select=True)    # noqa: E702
from flask_script import Manager, Shell
from bugsnag.flask import handle_exceptions


# Configure bugnsag
bugsnag.configure(
  api_key=os.getenv('BUGSNAG_API_TOKEN'),
  release_stage="development",
  project_root="app"
)


# local imports
from app import create_app, socketio  # noqa: E402


app = create_app(os.getenv('APP_SETTINGS') or 'default')
handle_exceptions(app)
manager = Manager(app)


def make_shell_context():
    socketio.run(app,
                 host='127.0.0.1',
                 port=5000, debug=True,)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context()))


if __name__ == '__main__':
    manager.run()
