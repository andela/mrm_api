#!/bin/bash

# get build status and branch
# send notification

STATUS=$1 #job status

get_build_report() {
  if [ "$CIRCLE_JOB" == 'test' -a  "$STATUS" == 'success' ]; then

    MESSAGE_TEXT="Test Phase Passed! :smiley:"
    COLOR="good"

  elif [ "$CIRCLE_JOB" == 'test' -a  "$STATUS" == 'fail' ]; then

    MESSAGE_TEXT="Test Phase Failed :scream:"
    COLOR="danger"
    REBUILD_URL="https://circleci.com/actions/retry/github/andela/mrm_front/${CIRCLE_BUILD_NUM}"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"


  elif [ "$CIRCLE_JOB" == 'deploy-job' -a "$STATUS" == 'success' ]; then

    MESSAGE_TEXT="Deployment Phase Succeeded :rocket:"
    COLOR="good"

  elif [ "$CIRCLE_JOB" == 'deploy-job' -a  "$STATUS" == 'fail' ]; then

    MESSAGE_TEXT="Deployment Phase Failed  :scream:"
    REBUILD_URL="https://circleci.com/actions/retry/github/andela/mrm_front/${CIRCLE_BUILD_NUM}"
    ACTION_BUTTON="$(echo \
          "{\"type\": \"button\", \"text\": \"Rebuild\", \"url\": \"${REBUILD_URL}\"}", \
      )"
    COLOR="danger"

  fi

  # prepare template for slack messaging
  COMMIT_LINK="https://github.com/${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}/commit/${CIRCLE_SHA1}"
  IMG_TAG="$(git rev-parse --short HEAD)"
  CIRCLE_WORKFLOW_URL="https://circleci.com/workflow-run/${CIRCLE_WORKFLOW_ID}"
  SLACK_TEXT_TITLE="CircleCI Build #$CIRCLE_BUILD_NUM"
  SLACK_DEPLOYMENT_TEXT="Executed Git Commit <$COMMIT_LINK|${IMG_TAG}>: ${MESSAGE_TEXT}"

}

send_notification() {
  curl -X POST --data-urlencode \
  "payload={
      \"channel\": \"${BUILD_CHANNEL}\",
      \"username\": \"DeployNotification\",
      \"attachments\": [{
          \"fallback\": \"CircleCI build notification\",
          \"color\": \"${COLOR}\",
          \"author_name\": \"Branch: $CIRCLE_BRANCH by ${CIRCLE_USERNAME}\",
          \"author_link\": \"https://github.com/AndelaOSP/art-android/tree/${CIRCLE_BRANCH}\",
          \"title\": \"${SLACK_TEXT_TITLE}\",
          \"title_link\": \"$CIRCLE_WORKFLOW_URL\",
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
