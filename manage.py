import os

import bugsnag
from flask_script import Manager, Shell
from bugsnag.flask import handle_exceptions

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


# Configure bugnsag
bugsnag.configure(
    api_key=os.getenv('BUGSNAG_API_TOKEN'),
    release_stage="development",
    project_root="app"
)

# local imports
from app import create_app  # noqa: E402

app = create_app(os.getenv('APP_SETTINGS') or 'default')
handle_exceptions(app)
manager = Manager(app)


def make_shell_context():
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print("Serving at host 0.0.0.0: 5000...\n")
    return server.serve_forever()


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context()))


if __name__ == '__main__':
    manager.run()
