#! /usr/bash

STATUS=$1

upload_deployment_report() {
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> retrieve csv >>>>>>>>>>>>>>>>>>"
  gsutil cp gs://deployment_report/deployment_report_backend.csv ./deployment_report_backend.csv
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> update csv >>>>>>>>>>>>>>>>>>>>"
  python ~/project/.circleci/update_csv.py $CIRCLE_BRANCH $STATUS
  echo  ">>>>>>>>>>>>>>>>>>>>>>>>>> update bucket >>>>>>>>>>>>>>>>>>>>"
  gsutil cp ./deployment_report_backend.csv gs://deployment_report/deployment_report_backend.csv
}

upload_deployment_report