#!/bin/bash
#while ! nc -z database 6379; do
#  sleep 0.1
#done
cd /app
export $(cat .env | xargs)
celery worker -A cworker.celery --loglevel=info
