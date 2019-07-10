#!groovy​

pipeline {
  agent {
    kubernetes {
      label 'mrm-api'
      defaultContainer 'jnlp'
      yamlFile './jenkins/config.yml'
    }
  }
  environment {
    PROJECT_NAME = 'mrm-api'
    APP_SETTINGS = 'testing'
    POSTGRES_DB = 'mrm_test_db'
  }
  stages {
        stage('Setup environment') {
          steps {
            container('mrm-api') {
              withCredentials([
                file(credentialsId: 'mrm-api-environments-silas', variable: 'CONVERGE_API_TEST')
              ]) {
                load "$CONVERGE_API_TEST"
              }
              sh "chmod +x jenkins/scripts/*.sh"
              sh "${WORKSPACE}/jenkins/scripts/setup.sh"
              sh "${WORKSPACE}/jenkins/scripts/setup_gcloud.sh"
              sh "curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ${WORKSPACE}/cc-test-reporter"
              sh "chmod +x ${WORKSPACE}/cc-test-reporter"
              sh """
                 python -m venv env
                 . env/bin/activate
                 pip install -U setuptools
                 pip install -r requirements.txt
              """
            }
          }
        }
        stage('test-3.6-flake') {
          steps {
            container('mrm-api') {
              sh """
                . env/bin/activate
                tox -e python3.6
                tox -e flake8
                coverage xml
              """
              sh "${WORKSPACE}/jenkins/scripts/upload_coverage.sh python3.6"
            }
          }
          post{
            success{
              container('mrm-api'){
                sh script:"${WORKSPACE}/jenkins/scripts/notify_slack.sh success", label: "Notify slack(success)"
              }
            }
            failure {
              container('mrm-api'){
                sh script: "${WORKSPACE}/jenkins/scripts/notify_slack.sh fail"
              }
            }
          }
         }
        stage('Clear database'){
          steps{
            container('mrm-db'){
              sh "su postgres -c \"dropdb $POSTGRES_DB\""
              sh "su postgres -c \"createdb $POSTGRES_DB\""
            }
          }
        }
        stage('test-3.5') {
          steps {
            container('mrm-api') {
              sh """
                . env/bin/activate
                tox -e python3.5
                coverage xml
              """
              sh "${WORKSPACE}/jenkins/scripts/upload_coverage.sh python3.5"
            }
          }
          post{
            success{
              container('mrm-api'){
                sh script:"${WORKSPACE}/jenkins/scripts/notify_slack.sh success", label: "Notify slack(success)"
              }
            }
            failure {
              container('mrm-api'){
                sh script: "${WORKSPACE}/jenkins/scripts/notify_slack.sh fail"
              }
            }
          }
        }

        stage("codeclimate-reporting"){
          steps{
            container('mrm-api'){
              sh "${WORKSPACE}/jenkins/scripts/retrieve_codeclimate_reports.sh"
              sh "${WORKSPACE}/jenkins/scripts/get_test_results.sh"
            }
          }
          post{
            success{
              container('mrm-api'){
                sh script:"${WORKSPACE}/jenkins/scripts/notify_slack.sh success", label: "Notify slack(success)"
              }
            }
            failure {
              container('mrm-api'){
                sh script: "${WORKSPACE}/jenkins/scripts/notify_slack.sh fail"
              }
            }
          }
        }

        stage("build_backend_image"){
          when { anyOf { branch 'v2'; branch 'develop'; branch 'master'} }
          steps{
            container("mrm-api"){
              withCredentials([string(credentialsId: 'mrm-github-repo-token', variable: 'GITHUB_REPO_TOKEN')]){
                sh "${WORKSPACE}/jenkins/scripts/set_environment_variables.sh"
                 sh "${WORKSPACE}/jenkins/scripts/build_image.sh"
              }
              
            }
          }
          post{
            success{
              container('mrm-api'){
                sh script:"${WORKSPACE}/jenkins/scripts/notify_slack.sh success", label: "Notify slack(success)"
              }
            }
            failure {
              container('mrm-api'){
                sh script: "${WORKSPACE}/jenkins/scripts/notify_slack.sh fail"
              }
            }
          }
        }

        stage("deploy_backend_to_kubernetes"){
          when { anyOf { branch 'v2'; branch 'develop'; branch 'master'} }
          steps{
            container('mrm-api'){
              withCredentials([string(credentialsId: 'mrm-github-repo-token', variable: 'GITHUB_REPO_TOKEN')]){
                 sh "${WORKSPACE}/jenkins/scripts/deploy_backend_to_kubernetes.sh"
              }
              
            }
          }
          post{
            success{
              container('mrm-api'){
                sh script:"${WORKSPACE}/jenkins/scripts/notify_slack.sh success", label: "Notify slack(success)"
              }
            }
            failure {
              container('mrm-api'){
                sh script: "${WORKSPACE}/jenkins/scripts/notify_slack.sh fail"
              }
            }
          }
        }
  }
}
