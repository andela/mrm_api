#!/bin/bash

download_coverage_files_from_bucket(){
    GIT_HASH=$(echo "$GIT_COMMIT" | cut -c -7)
    mkdir -p parallel-coverage
    #Get the recently uploaded coverage from Google Cloud Bucket
    gsutil cp gs://parallel-coverage-reports/backend/python3.5/.coverage-$GIT_HASH \
      parallel-coverage/.coverage.3.5
    gsutil cp gs://parallel-coverage-reports/backend/python3.6/.coverage-$GIT_HASH \
      parallel-coverage/.coverage.3.6
    #Remove the .coverage file from GCP Bucket to free up space
    gsutil rm gs://parallel-coverage-reports/backend/python3.5/.coverage-$GIT_HASH
    gsutil rm gs://parallel-coverage-reports/backend/python3.6/.coverage-$GIT_HASH
}

download_coverage_files_from_bucket $@
