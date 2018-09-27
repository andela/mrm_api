import csv
import sys
import datetime

with open('deployment_report_backend.csv', 'a') as csv_file:
    # Get current date and time
    deployment_time = datetime.datetime.now()

    # assign python script argument as varables
    branch_name = sys.argv[1]
    deployment_status = sys.argv[2]

    # create new row
    new_data = [deployment_time, deployment_status, branch_name]

    # append the new row to the csv
    writer = csv.writer(csv_file)
    writer.writerow(new_data)
