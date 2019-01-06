import os
import eventlet; eventlet.monkey_patch(select=True) # noqa : E702

import bugsnag
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

if __name__ == '__main__':
    socketio.run()
