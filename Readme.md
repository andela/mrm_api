[![CircleCI](https://circleci.com/gh/andela/mrm_api.svg?style=svg)](https://circleci.com/gh/andela/mrm_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/33ed9630b4f81976f784/maintainability)](https://codeclimate.com/repos/5b0c1a7f82b58e02d000118e/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/33ed9630b4f81976f784/test_coverage)](https://codeclimate.com/repos/5b0c1a7f82b58e02d000118e/test_coverage)
## Product overview
 The MRM-api is the backbone of a tool to facilitate room management. It enables  capturing of feedback based on room usage and analyse usage statistics.The MRM-api provides capability to register rooms and give feedback.

## Development set up

#### Set up with docker
- Install docker
	```
    brew cask install docker
    ```
    OR
    
    [install via dmg file](https://docs.docker.com/docker-for-mac/install/)
    
- Create Application environment variables and save them in .env file
    ```
    APP_SETTINGS="testing" # set app Enviroment.
    SECRET_KEY="some-very-long-string-of-random-characters"
    DEV_DATABASE_URL="" # Db for Development.
    TEST_DATABASE_URL="" # Db for Testing
    DATABASE_URL="" # Db for Production
    MAIL_SERVER=""# SMTP server
    MAIL_PORT="" # server port
    MAIL_USE_TLS="" # Using TLS?
    MAIL_USERNAME="" # converge username
    MAIL_PASSWORD="" # password
    CELERY_BROKER_URL="" # redis url
    CELERY_RESULT_BACKEND="" # redis url
    C_FORCE_ROOT=true
    ```
- Run application.
    ```
    make build
    ```
    This will create 3 services
    	
     - database
     - app
     - redis

    Start the gunicorn server
    ```
    make run-app
    ```
- Running migrations

    - Initial migration commands
        ```
        make migrate-initial message="Migration message"
        ```
    - If you have one migration file in the alembic/version folder. Run the commands below:
        ```
        make migrate
        ```
    - If you have more than 2 migration files in the alembic/versions folder. Rum the commands bellow
        ```
        make migrate message="Migration message"
        ```
- Show services
	```
    make services
    ```
- Check the status
	```
    make status
    ```
- Start services individually
	```
    make start service=<service name>
    ```
- Create services individually
	```
    make create service=<service name>
    ```
- Stop all services
	```
    make down
    ```
- Stop services individually
	```
    make stop service=<service name>
    ```
- Remove services individually
	```
    make remove service=<service name>
    ```
- Restarting a service
	```
    make restart service=<service name>
    ```
- Kill services
	```
    make kill
    ```
- Remove a container
	```
    make remove
    ```
- SSH into a container
	```
    make ssh service=<service name>
    ```
- Running Tests

  - Create Application environment variables and save them in .env.tests file. Do not include comments
    ```
    APP_SETTINGS="testing" # set app Enviroment.
    SECRET_KEY="some-very-long-string-of-random-characters"
    DEV_DATABASE_URL="" # Db for Development.
    TEST_DATABASE_URL="" # Db for Testing
    DATABASE_URL="" # Db for Production
    MAIL_SERVER=""# SMTP server
    MAIL_PORT="" # server port
    MAIL_USE_TLS="" # Using TLS?
    MAIL_USERNAME="" # converge username
    MAIL_PASSWORD="" # password
    CELERY_BROKER_URL="" # redis url
    CELERY_RESULT_BACKEND="" # redis url
    C_FORCE_ROOT=true
    ADMIN_TOKEN=""
    USER_TOKEN=""
    INVALID_TOKEN=""
    ```
  - create database for tests
 	```
    make create-test-database
    ```
  - stop the redis service
    ```
    make stop service=redis
    ```
  - To run tests and observe test coverage for various versions of python . Run the command below.
	```
 	make test test=tox
 	```
  - To run  and check for test coverage. Run the command below:
 	```
 	make test test="coverage run -m pytest"
 	```
  - To obtain coverage report. Run the command below:

 	```
 	make test test="coverage report"
 	```
  - To obtain html browser report. Run command below:
 	```
	make test test="coverage html"
 	```
 	```
 	A folder titled html_coverage_report will be generated. Open it and copy the path  of index.html and paste it in your browser.
 	```
  - To run lint tests with `flake8`:

 	```
 	make test test="flake8"
 	```

##### Importing a database dump to the docker database container
  - Create a dump from a database, preferrably `--no-owner` flag
	```
	pg_dump -d <dbname> -U <postgres-user> -h <localhost/ipaddress> --no-owner -F p --column-inserts > converge.sql
	```
  - Import the database
  	```
    make import dump="<path to dump file>"
  	```

#### Set up without docker

- Check that python 3, pip, virtualenv and postgress are installed

- Check that python 3, pip, virtualenv and postgress are installed

- Clone the mrm-api repo and cd into it
    ```
    git clone https://github.com/andela/mrm_api.git
    ```
- Create virtual env
    ```
    virtualenv --python=python3 venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Create Application environment variables and save them in .env file
    ```
    export APP_SETTINGS="development" # set app Enviroment.
    export SECRET_KEY="some-very-long-string-of-random-characters"
    export DEV_DATABASE_URL="" # Db for Development.
    export TEST_DATABASE_URL="" # Db for Testing
    export DATABASE_URL="" # Db for Production
    ```
- Running migrations

    - Initial migration commands
        ```
        $ alembic revision --autogenerate -m "Migration message"

        $ alembic upgrade head
        ```
    - If you have one migration file in the alembic/version folder. Run the commands below:
        ```
        $ alembic stamp head

        $ alembic upgrade head
        ```
    - If you have more than 2 migration files in the alembic/versions folder. Rum the commands bellow
        ```
        $ alembic stamp head

        $ alembic upgrade head

        $ alembic revision --autogenerate -m "Migration message"
        
        $ alembic upgrade head
        
        ```
- Running asynchronous functionalities.

    - Install redis with running the redis bash file `run-redis.sh`, this will also run the redis server (*Celery Message Broker*) for the first time.

    - To run redis after it has been stopped run `redis-server`

    - In a new terminal tab run the **Celery Message Worker** as:
    ```
    celery worker -A cworker.celery --loglevel=info
    ```
    
- Run application.
    ```
    python manage.py runserver
    ```

- Running Tests
 - To run tests and observe test coverage for various versions of python . Run the command below.
 ```
 tox
 ```
 - To run  and check for test coverage. Run the command below:
 ```
 coverage run -m pytest
 ```
 - To obtain coverage report. Run the command below:

 ```
 coverage report
 ```
 - To obtain html browser report. Run command below:
 ```
 coverage html
 ```
 ```
 A folder titled html_coverage_report will be generated. Open it and copy the path  of index.html and paste it in your browser.
 ```

## Built with
- Python version  3
- Flask
- Grapghql
- Postgres

## Contribution guide
##### Contributing
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a [Pivotal Tracker board](https://www.pivotaltracker.com/n/projects/2154921) to track  the work done.

 ##### Pull Request Process
- A contributor shall identify a task to be done from the [pivotal tracker](https://www.pivotaltracker.com/n/projects/2154921).If there is a bug , feature or chore that has not be included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
- The Contributor shall then create a branch off  the ` develop` branch where they are expected to undertake the task they have chosen.
- After  undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
- If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owners of this repository.
