#!/bin/bash
cd /app
export $(cat .env | xargs)
# run migrations
alembic upgrade head
# run gunicorn
gunicorn manage:app --worker-class gevent -b 0.0.0.0:8000 --reload --log-syslog
