#!/bin/bash
generate_image_environment_variables() {
    echo '' > .env
    #Set deployment image environment variables
    echo "APP_SETTINGS"=$(echo $IMAGE_APP_SETTINGS) >> .env
    echo "ANDELA_LOGIN_URL"=$(echo $IMAGE_ANDELA_LOGIN_URL) >> .env
    echo "ANDELA_API_URL"=$(echo $IMAGE_ANDELA_API_URL) >> .env
    echo "PROD_REQUEST_URL"=$(echo $PROD_REQUEST_URL) >> .env
    if [ "$GIT_BRANCH" == master ]; then
      echo "DEV_DATABASE_URL"=$(echo $IMAGE_DEV_DATABASE_URL_PRODUCTION) >> .env
      echo "DATABASE_URL"=$(echo $IMAGE_DATABASE_URL_PRODUCTION) >> .env
      echo "CELERY_BROKER_URL"=$(echo $IMAGE_CELERY_BROKER_URL_PRODUCTION) >> .env
      echo "CELERY_RESULT_BACKEND"=$(echo $IMAGE_CELERY_RESULT_BACKEND_PRODUCTION) >> .env
      echo "MRM_PUSH_URL"=$(echo $IMAGE_MRM_PUSH_URL_PRODUCTION) >> .env
    elif [ "$GIT_BRANCH" == develop ]; then
      echo "DEV_DATABASE_URL"=$(echo $IMAGE_DEV_DATABASE_URL_STAGING) >> .env
      echo "DATABASE_URL"=$(echo $IMAGE_DATABASE_URL_STAGING) >> .env
      echo "CELERY_BROKER_URL"=$(echo $IMAGE_CELERY_BROKER_URL_STAGING) >> .env
      echo "CELERY_RESULT_BACKEND"=$(echo $IMAGE_CELERY_RESULT_BACKEND_STAGING) >> .env
      echo "MRM_PUSH_URL"=$(echo $IMAGE_MRM_PUSH_URL_STAGING) >> .env
    else
      echo "DEV_DATABASE_URL"=$(echo $IMAGE_DEV_DATABASE_URL_SANDBOX) >> .env
      echo "DATABASE_URL"=$(echo $IMAGE_DATABASE_URL_SANDBOX) >> .env
      echo "CELERY_BROKER_URL"=$(echo $IMAGE_CELERY_BROKER_URL_SANDBOX) >> .env
      echo "CELERY_RESULT_BACKEND"=$(echo $IMAGE_CELERY_RESULT_BACKEND_SANDBOX) >> .env
      echo "MRM_PUSH_URL"=$(echo $IMAGE_MRM_PUSH_URL_SANDBOX) >> .env
    fi
    echo "SECRET_KEY"=$(echo $IMAGE_SECRET_KEY) >> .env
    echo "MAIL_SERVER"=$(echo $IMAGE_MAIL_SERVER) >> .env
    echo "MAIL_PORT"=$(echo $IMAGE_MAIL_PORT) >> .env
    echo "MAIL_USE_TLS"=$(echo $IMAGE_MAIL_USE_TLS) >> .env
    echo "MAIL_USERNAME"=$(echo $IMAGE_MAIL_USERNAME) >> .env
    echo "MAIL_PASSWORD"=$(echo $IMAGE_MAIL_PASSWORD) >> .env
    echo "C_FORCE_ROOT=true" >> .env
}

generate_image_environment_variables $@