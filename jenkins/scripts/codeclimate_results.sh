#!/bin/bash
retrieve_and_combine_test_results(){
    ${WORKSPACE}/cc-test-reporter before-build
    . ${WORKSPACE}/env/bin/activate
    coverage combine parallel-coverage/ 
    coverage xml
    coverage report
    ${WORKSPACE}/cc-test-reporter format-coverage -o ./.coverage -t coverage.py
    ${WORKSPACE}/cc-test-reporter upload-coverage -i .coverage
}

retrieve_and_combine_test_results $@
