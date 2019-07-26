#!/usr/bin/env  bash

build_and_push_image(){
    export PATH=$PATH:/usr/local/gcloud/google-cloud-sdk/bin
    GIT_HASH=$(echo $GIT_COMMIT | cut -c -7)
    if [ "$GIT_BRANCH" == master ]; then
      docker login -u _json_key -p "$(echo $GOOGLE_CREDENTIALS_STAGING | base64 -d )" https://gcr.io
      gsutil cp gs://${BACKEND_BASE_IMAGE_VERSION_PATH_PRODUCTION}current_version .
      VERSION=$(cat current_version)
      export IMAGE=$BACKEND_BASE_IMAGE_PRODUCTION:$VERSION
      sed -i "s|{{IMAGE}}|$IMAGE|g" docker/prod/Dockerfile
      docker build -f docker/prod/Dockerfile -t ${PRODUCTION_BACKEND_IMAGE}:$GIT_HASH .
      docker push ${PRODUCTION_BACKEND_IMAGE}:$GIT_HASH
      touch current_version
      echo ${GIT_HASH} > current_version
      gsutil cp current_version gs://${PRODUCTION_BACKEND_IMAGE_VERSION_PATH}
    elif [ "$GIT_BRANCH" == develop ]; then
      docker login -u _json_key -p "$(echo $GOOGLE_CREDENTIALS_STAGING | base64 -d )" https://gcr.io
      gsutil cp gs://${BACKEND_BASE_IMAGE_VERSION_PATH_STAGING}current_version .
      VERSION=$(cat current_version)
      export IMAGE=$BACKEND_BASE_IMAGE_STAGING:$VERSION
      sed -i "s|{{IMAGE}}|$IMAGE|g" docker/prod/Dockerfile
      docker build -f docker/prod/Dockerfile -t ${STAGING_BACKEND_IMAGE}:$GIT_HASH .
      docker push ${STAGING_BACKEND_IMAGE}:$GIT_HASH
      touch current_version
      echo ${GIT_HASH} > current_version
      gsutil cp current_version gs://${STAGING_BACKEND_IMAGE_VERSION_PATH}
    else
      docker login -u _json_key -p "$(echo $GOOGLE_CREDENTIALS_STAGING | base64 -d )" https://gcr.io
      gsutil cp gs://${BACKEND_BASE_IMAGE_VERSION_PATH_SANDBOX}current_version .
      VERSION=$(cat current_version)
      export IMAGE=$BACKEND_BASE_IMAGE_SANDBOX:$VERSION
      sed -i "s|{{IMAGE}}|$IMAGE|g" docker/prod/Dockerfile
      docker build -f docker/prod/Dockerfile -t ${SANDBOX_BACKEND_IMAGE}:$GIT_HASH .
      docker push ${SANDBOX_BACKEND_IMAGE}:$GIT_HASH
      touch current_version
      echo ${GIT_HASH} > current_version
      gsutil cp current_version gs://${SANDBOX_BACKEND_IMAGE_VERSION_PATH}
    fi
}

build_and_push_image $@