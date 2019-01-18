#!/bin/bash
while ! nc -z database 5432; do
  sleep 0.1
done
cd /app
export $(cat .env | xargs)
MESSAGE="$@"
if [ -z "$MESSAGE" ] 
then
	alembic stamp head
	alembic upgrade head
else
	alembic stamp head
	alembic upgrade head
    alembic revision --autogenerate -m "$MESSAGE"
	alembic upgrade head
fi
