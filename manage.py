import os

from flask_script import Manager, Shell

# local imports
from app import create_app


app = create_app(os.getenv('APP_SETTINGS') or 'default')
<<<<<<< HEAD
=======
# migrate = Migrate(app, db)
>>>>>>> ae12050f... [Chore #156466913] Refact automation file
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command(
    "shell", Shell(
        make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
