import os
from celery import Celery
from app import create_app


app = create_app(os.getenv('APP_SETTINGS') or 'default')
app.app_context().push()


app.config.update(
    CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL'),
    CELERY_RESULT_BACKEND=os.getenv('CELERY_RESULT_BACKEND'),
    CELERY_ACCEPT_CONTENT=['pickle']
)


def make_celery(app):
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], include=['admin_notifications.helpers.create_notification'], # noqa 501
                    backend=app.config['CELERY_BROKER_URL'])

    celery.conf.update(app.config)
    celery.conf.enable_utc = False
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


celery = make_celery(app)
celery_scheduler = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery_scheduler.conf.update(app.config)
