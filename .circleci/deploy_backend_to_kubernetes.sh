#!/usr/bin/env bash

checkout_deployment_scripts() {
    if [ "$CIRCLE_BRANCH" == "master" ]; then
        git clone -b master https://github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    elif [ "$CIRCLE_BRANCH" == "develop" ]; then
        git clone -b develop https://github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    else
        git clone -b k8s-sandbox https://github.com/andela/mrm-deployment-scripts.git ${HOME}/deployments
    fi
}

terraform_values() {
    cd ${HOME}/deployments/
    mkdir -p secrets
    . supply_values.sh
}

run_terraform() {
    cd ${HOME}/deployments/
    . .circleci/deploy_to_kubernetes.sh
    deploy
    cat secrets/ssl_andela_certificate.crt
    cat secrets/ssl_andela_key.key
}

main() {
    checkout_deployment_scripts
    terraform_values
    run_terraform
}

main #@
