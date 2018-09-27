import csv
import sys
import pprint

# Function to convert a csv file to a list of dictionaries

def csv_dict_list(csv_file):
    reader = csv.DictReader(open(csv_file, 'rt'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

# Calls the csv_dict_list function, passing the named csv

count = csv_dict_list(sys.argv[1])

pprint.pprint(count[0].get("time"))
