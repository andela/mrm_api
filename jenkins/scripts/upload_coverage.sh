#!/bin/bash

upload_coverage_files_to_gcp(){
    #Set GIT_HASH to the first 7 characters of the git commit hash
    GIT_HASH=$(echo $GIT_COMMIT | cut -c -7)
    #Copy the coverage file to the GCP Bucket
    gsutil cp .coverage gs://parallel-coverage-reports/backend/$1/.coverage-$GIT_HASH
}

upload_coverage_files_to_gcp $@
