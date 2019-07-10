#!/usr/bin/env bash

setup_and_authenticate_to_gcp(){
    # store Service Account Key into file
    echo $GCLOUD_SERVICE_KEY | base64 --decode > ${HOME}/gcloud-service-key.json
    #Activate the service account
    gcloud auth activate-service-account --key-file ${HOME}/gcloud-service-key.json
    gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
    gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}
}

setup_and_authenticate_to_gcp $@
