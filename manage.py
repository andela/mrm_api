import os

from flask_script import Manager, Shell

# local imports
from app import create_app


app = create_app(os.getenv('APP_SETTINGS') or 'default')
# migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
