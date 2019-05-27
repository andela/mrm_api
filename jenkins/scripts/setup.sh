#!/bin/bash

generate_mock_test_data(){
    #Create test data and decode credentials
    echo $CREDENTIALS | base64 --decode > credentials.json
    echo $TEST_CREDENTIALS | base64 --decode > users.json
    echo $CALENDAR_LIST1$CALENDAR_LIST2 | base64 --decode > calendar_list.json
    echo $EVENTS | base64 --decode > events.json
}

generate_mock_test_data $@
