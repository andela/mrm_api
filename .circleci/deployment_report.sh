#! /usr/bash

get_report() {
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> retrieve csv >>>>>>>>>>>>>>>>>>"
  gsutil cp gs://deployment_report/deployment_report_test.csv ./deployment_report_test.csv
  STARTDATE="$(date --date="7 days ago" '+%Y-%m-%d')"
  ENDDATE=$(date '+%Y-%m-%d %H:%M:%S')
  FAILED_DEPLOYMENT=$(querycsv.py -i deployment_report_test.csv "select time, status from deployment_report_test where time between '${STARTDATE}' and '${ENDDATE}' and status = 'failed'")
  SUCCESS_DEPLOYMENT=$(querycsv.py -i deployment_report_test.csv "select time, status from deployment_report_test where time between '${STARTDATE}' and '${ENDDATE}' and status = 'succeeded'")
  FAILED_COUNT=$(( $(echo "$FAILED_DEPLOYMENT" | wc -l) - 2 ))
  SUCCESS_COUNT=$(( $(echo "$SUCCESS_DEPLOYMENT" | wc -l) - 2 ))

  DEPLOYMENT_REPORT_MESSAGE="Hi Team.\n
Here is the deployment report for the week.\n
Between ${STARTDATE} and ${ENDDATE},\n
we had ${SUCCESS_COUNT} successful deployments and ${FAILED_COUNT} Failed deployments.\n
In Converge-Backend :devops:"
}


send_notification() {

  # Sending the Slack notification

  curl -X POST --data-urlencode \
  "payload={
      \"channel\": \"${DEPLOYMENT_SLACK_CHANNEL}\",
      \"username\": \"DeployNotification\",
      \"attachments\": [{
          \"fallback\": \"CircleCI Deployment Notification\",
          \"color\": \"good\",
          \"title\": \"Deployment Report\",
          \"text\": \"${DEPLOYMENT_REPORT_MESSAGE}\",
      }]
  }" \
  "${SLACK_WEB_HOOK}"
}

main() {
  get_report
  send_notification
}

main