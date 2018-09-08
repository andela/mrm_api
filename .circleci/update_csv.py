import csv
import sys
import datetime

with open('deployment_report_test.csv', 'a') as csv_file:
    deployment_time = datetime.datetime.now()
    branch_name = sys.argv[1]
    deployment_status = sys.argv[2]
    new_data = [deployment_time, deployment_status, branch_name]
    writer = csv.writer(csv_file)
    writer.writerow(new_data)
