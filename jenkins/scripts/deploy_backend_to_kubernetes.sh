#!/usr/bin/env bash

checkout_deployment_scripts() {
    #Clone the deployment scripts repo
    if [ "$GIT_BRANCH" == "master" ]; then
        git clone -b master https://$GITHUB_REPO_TOKEN@github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    elif [ "$GIT_BRANCH" == "develop" ]; then
        git clone -b develop https://$GITHUB_REPO_TOKEN@github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    else
        git clone -b k8s-sandbox https://$GITHUB_REPO_TOKEN@github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    fi
}

terraform_values() {
    #Generate values for terraform variables
    cd ${HOME}/deployments/
    mkdir -p ${HOME}/deployments/secrets
    echo $CERTIFICATE | base64 -d > ${HOME}/deployments/secrets/ssl_andela_certificate.crt
    echo $KEY | base64 -d > ${HOME}/deployments/secrets/ssl_andela_key.key
    # Substitute environment variable names in the deployment scripts that are
    # specific to CIRCLECI to match Jenkins
    sed -i -- 's/base64 --decode/base64 -d/g' ${HOME}/deployments/.circleci/deploy_to_kubernetes.sh
    sed -i -- 's/CIRCLE_BRANCH/GIT_BRANCH/g' ${HOME}/deployments/.circleci/deploy_to_kubernetes.sh
    sed -i -- 's/CIRCLE_BRANCH/GIT_BRANCH/g' ${HOME}/deployments/supply_values.sh
    . supply_values.sh
}

run_terraform() {
    # Run terraform commands
    cd ${HOME}/deployments/
    # Substitute environment variable names in the deployment scripts that are
    # specific to CIRCLECI to match Jenkins
    sed -i -- 's/base64 --decode/base64 -d/g' ${HOME}/deployments/.circleci/deploy_to_kubernetes.sh
    sed -i -- 's/CIRCLE_BRANCH/GIT_BRANCH/g' ${HOME}/deployments/.circleci/deploy_to_kubernetes.sh
    . .circleci/deploy_to_kubernetes.sh
    deploy $(echo $GIT_BRANCH)
}

main() {
    checkout_deployment_scripts
    terraform_values
    run_terraform
}

main #@