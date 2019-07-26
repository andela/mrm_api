#!/bin/bash
function add_env_variables(){
    # activate virtual environment
    . ${WORKSPACE}/env/bin/activate
    # set up .env file
    touch .env
    gsutil cp gs://converge/secrets/jenkins/api_env.txt .env
    source .env
    # Add mock test data
    echo $CREDENTIALS | base64 --decode > credentials.json
    echo $TEST_CREDENTIALS | base64 --decode > users.json
    echo $CALENDAR_LIST | base64 --decode > calendar_list.json
    echo $EVENTS | base64 --decode > events.json
    # Run tests
    . env/bin/activate
    if [ "$STAGE_NAME" == "test-3.5" ]; then
        tox -e python3.5
        coverage xml
    elif [ "$STAGE_NAME" == "test-3.6-flake" ]; then
        tox -e python3.6
        tox -e flake8
        coverage xml
    fi
}
add_env_variables