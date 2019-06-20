#!/bin/bash
cd /app
export $(cat .env | xargs)
celery worker -A cworker.celery --loglevel=info &
celery -A cworker.celery beat -l info
