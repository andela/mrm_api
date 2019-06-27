#!/usr/bin/env bash

# get build status and branch
# send notification

STATUS=$1 #job status
REBUILD_URL="https://jenkins.andela.com/blue/organizations/jenkins/Converge-Backend/detail/${GIT_BRANCH}/${BUILD_NUMBER}/pipeline"
GIT_USERNAME="$(git show -s --pretty=%an)"
get_build_report() {
  #Send a slack notification with the status of each stage
  if [[ "$STAGE_NAME" == "test-3.6-flake" ]] && [[  "$STATUS" == 'success' ]]; then

    MESSAGE_TEXT="${STAGE_NAME} Phase Passed! :smiley:"
    COLOR="good"

  elif [[ "$STAGE_NAME" == "test-3.6-flake" ]] && [[  "$STATUS" == 'fail' ]]; then

    MESSAGE_TEXT="${STAGE_NAME} Phase Failed :scream:"
    COLOR="danger"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"
  elif [[ "$STAGE_NAME" == "test-3.5" ]] && [[  "$STATUS" == 'success' ]]; then

    MESSAGE_TEXT="${STAGE_NAME} Phase Passed! :smiley:"
    COLOR="good"
  elif [[ "$STAGE_NAME" == "test-3.5" ]] && [[  "$STATUS" == 'fail' ]]; then

    MESSAGE_TEXT="${STAGE_NAME} Phase Failed :scream:"
    COLOR="danger"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"

  elif [ "$STAGE_NAME" == 'codeclimate-reporting' -a  "$STATUS" == 'success' ]; then

    MESSAGE_TEXT="Code climate Phase Passed! :smiley:"
    COLOR="good"

  elif [ "$STAGE_NAME" == 'codeclimate-reporting' -a  "$STATUS" == 'fail' ]; then

    MESSAGE_TEXT="Code climate Phase Failed :scream:"
    COLOR="danger"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"

  elif [ "$STAGE_NAME" == 'build_backend_image' -a "$STATUS" == 'success' ]; then

    MESSAGE_TEXT="Image building phase Succeeded:rocket:"
    COLOR="good"

  elif [ "$STAGE_NAME" == 'build_backend_image' -a  "$STATUS" == 'fail' ]; then

    MESSAGE_TEXT="Image building phase Failed  :scream:"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"
    COLOR="danger"
  elif [ "$STAGE_NAME" == 'deploy_backend_to_kubernetes' -a "$STATUS" == 'success' ]; then

    MESSAGE_TEXT="Deployment Phase Succeeded :rocket:"
    COLOR="good"

  elif [ "$STAGE_NAME" == 'deploy_backend_to_kubernetes' -a  "$STATUS" == 'fail' ]; then

    MESSAGE_TEXT="Deployment Phase Failed  :scream:"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"
    COLOR="danger"

  fi


  # prepare template for slack messaging
  COMMIT_LINK="https://github.com/andela/mrm_api/commit/$GIT_COMMIT"
  IMG_TAG="$(git rev-parse --short HEAD)"
  SLACK_TEXT_TITLE="Jenkins Build #$BUILD_NUMBER"
  SLACK_DEPLOYMENT_TEXT="Executed Git Commit <$COMMIT_LINK|${IMG_TAG}>: ${MESSAGE_TEXT}"

}

# send notification to slack
send_notification() {
  curl -X POST --data-urlencode \
  "payload={
      \"channel\": \"${BUILD_CHANNEL}\",
      \"username\": \"DeployNotification\",
      \"attachments\": [{
          \"fallback\": \"Jenkins build notification\",
          \"color\": \"${COLOR}\",
          \"author_name\": \"Branch: $GIT_BRANCH by ${GIT_USERNAME}\",
          \"author_link\": \"https://github.com/andela/mrm_api/tree/${GIT_BRANCH}\",
          \"title\": \"${SLACK_TEXT_TITLE}\",
          \"title_link\": \"$REBUILD_URL\",
          \"text\": \"${SLACK_DEPLOYMENT_TEXT}\",
          \"actions\": [${ACTION_BUTTON}]
      }]
  }" \
  "${BUILD_CHANNEL_WEBHOOK}"
}

main() {
  get_build_report
  send_notification
}

main