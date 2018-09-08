#! /usr/bash

STATUS=$1

upload_deployment_report() {
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> retrieve csv >>>>>>>>>>>>>>>>>>"
  gsutil cp gs://deployment_report/deployment_report_test.csv ./deployment_report_test.csv
  echo ">>>>>>>>>>>>>>>>>>>>>>>>>> update csv >>>>>>>>>>>>>>>>>>>>"
  python ~/project/.circleci/update_csv.py $CIRCLE_BRANCH $STATUS
  echo  ">>>>>>>>>>>>>>>>>>>>>>>>>> update bucket >>>>>>>>>>>>>>>>>>>>"
  gsutil cp ./deployment_report_test.csv gs://deployment_report/deployment_report_test.csv
}

upload_deployment_report