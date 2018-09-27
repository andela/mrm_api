#! /usr/bash

get_report() {
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> retrieve csv >>>>>>>>>>>>>>>>>>"
  gsutil cp gs://deployment_report/deployment_report_backend.csv ./deployment_report_backend.csv

  # get start date and end date
  STARTDATE="$(date --date="7 days ago" '+%Y-%m-%d %H:%M')"
  ENDDATE=$(date '+%Y-%m-%d %H:%M:%S')

  # query csv file for failed and successful deployment
querycsv.py -i deployment_report_backend.csv -o failed.csv "select count(*) time, status from deployment_report_backend where time between '${STARTDATE}' and '${ENDDATE}' and status = 'failed'"
querycsv.py -i deployment_report_backend.csv -o passed.csv "select count(*) time, status from deployment_report_backend where time between '${STARTDATE}' and '${ENDDATE}' and status = 'succeeded'"



# get count of failed and successful deployment
FAILED_COUNT=$(python ~/project/.circleci/csv_parser.py failed.csv)
SUCCESS_COUNT=$(python ~/project/.circleci/csv_parser.py passed.csv)

  DEPLOYMENT_REPORT_MESSAGE="Hi Team.\n
Here is the deployment report for the week.\n
Between ${STARTDATE} and ${ENDDATE},\n
we had ${SUCCESS_COUNT} successful deployments and ${FAILED_COUNT} Failed deployments.\n
In Converge-Backend :devops:"
}

# send notification to slack
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