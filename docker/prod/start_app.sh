#!/bin/bash
cd /app
export $(cat .env | xargs)
# run migrations
alembic upgrade head
touch mrm.err.log
# run gunicorn
gunicorn --access-logfile 'mrm.err.log' --workers 2 -t 3600 manage:app --worker-class gevent -b 0.0.0.0:8000 --reload  &

function create_sock_file {
  touch /var/run/supervisor.sock
  chmod 777 /var/run/supervisor.sock
  service supervisor start
}

function run_celery {
  supervisorctl start celery
}

function main {
  create_sock_file
  run_celery
}

main $@
