#!/bin/bash
while ! nc -z database 5432; do
  sleep 0.1
done
cd /app
export $(cat .env | xargs)
gunicorn manage:app --worker-class gevent -b 0.0.0.0:8000 --reload --log-syslog
