import re


def read_log_file(log_file):
    """
    Function that accepts log file and opens it.
    Opens the file in reverse order, iterates through
    every line to return the logs.
    """
    timestamp_pattern = re.compile(r'(\d+-\d+-\d+ \d+:\d+:\d+)')
    error_details = []
    for line in reversed(list(open(log_file, 'r'))):
        if timestamp_pattern.search(line):  # check if line contains timestamp
            yield line
            for detail in reversed(error_details):
                yield detail
            error_details.clear()
        else:
            error_details.append(line)  # add error log details to a list
