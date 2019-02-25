#!/bin/bash
cd /app
export $(cat .env | xargs)
celery worker -A cworker.celery --loglevel=info
