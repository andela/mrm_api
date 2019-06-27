#!/usr/bin/env bash

setup_and_authenticate_to_gcp(){
    touch google-service-key.json
    # store Service Account Key into file
    echo $GCLOUD_SERVICE_KEY | base64 --decode > ${WORKSPACE}/google-service-key.json
    #Activate the service account
    gcloud auth activate-service-account --key-file ${WORKSPACE}/google-service-key.json
    gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
    gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}
}

setup_and_authenticate_to_gcp $@