# Define filename references
DEV_FOLDER := docker/dev
DEV_COMPOSE_FILE := docker/dev/docker-compose.yml

# Set target lists
.PHONE: help

help:
	@echo ''
	@echo 'Usage:'
	@echo '${YELLOW} make ${RESET} ${GREEN}<target> [options]${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		message = match(lastLine, /^## (.*)/); \
		if (message) { \
			command = substr($$1, 0, index($$1, ":")-1); \
			message = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} %s\n", command, message; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

build:
	@ echo "Building converge..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} up -d
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/start_app.sh

status:
	@ echo "Checking status..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} ps

create:
	@ echo 'Creating $(service) service...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} create $(service)

start:
	@ echo 'Starting  $(service) service...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} start $(service)

run-app:
	@ echo 'Running mrm_api on port 8000...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/start_app.sh

stop:
	@ echo 'Stopping $(service) service...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} stop $(service)

restart:
	@ echo 'restarting $(service) service...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} stop $(service)
	@ docker-compose -f ${DEV_COMPOSE_FILE} rm -f -v $(service)
	@ docker-compose -f ${DEV_COMPOSE_FILE} create --force-recreate $(service)
	@ docker-compose -f ${DEV_COMPOSE_FILE} start $(service)

migrate-initial:
	@ echo 'Running initial migrations...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/start_initial_migrations.sh "$(message)"

migrate:
	@ echo 'Running migrations...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/start_migrations.sh "$(message)"

import:
	@ echo "importing database..."
	@ docker cp ${DEV_FOLDER}/start_db_import.sh mrm_database:/
	@ docker cp $(dump) mrm_database:/
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec database /start_db_import.sh $(dump)

create-test-database:
	@ echo 'create test database...'
	@ docker cp ${DEV_FOLDER}/create_test_db.sh mrm_database:/
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec -u root database /create_test_db.sh

test:
	@ echo 'start tests...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec app ${DEV_FOLDER}/start_tests.sh "$(test)"

ssh:
	@ echo 'ssh...'
	@ docker-compose -f ${DEV_COMPOSE_FILE} exec $(service) /bin/bash

down:
	@ echo "Converge going down..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} down

services:
	@ echo "Getting services..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} ps --services

remove:
	@ echo "Removing $(service) container"
	@ docker-compose -f ${DEV_COMPOSE_FILE} rm -f -v $(service)

clean: down
	@ echo "Removing containers..."
	@ docker stop mrm_database mrm_api mrm_redis
	@ docker rm mrm_database mrm_api mrm_redis

kill:
	@ echo "killing..."
	@ docker-compose -f ${DEV_COMPOSE_FILE} kill -s SIGINT
