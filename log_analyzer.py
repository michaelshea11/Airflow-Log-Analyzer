"""This project is a simple log analyzer that will analyze the Airflow scheduler log 
associted with a seperate Repository on this Github."""

from datetime import datetime, timedelta, date
from pathlib import Path
import sys

base_log = "/Users/michaelshea/springboard_projects/airflow_marketvol_project/logs/scheduler/latest/marketvol_dag.py.log"

def analyze_log(base_log):
    file_list = Path(base_log).rglob('*.log')
    error_count = 0
    error_list = []
    for file in file_list:
        count, cur_list = analyze_file(file)
        error_count = error_count + count
        error_list.extend(cur_list)
    print("Total number of errors: {}".format(error_count))
    print("Here are all the errors:")
    for error in error_list:
        print(error)


def analyze_file(filename):
    file = open(filename, 'r')
    error_count = 0
    error_list = []
    lines = file.readlines()
    for line in lines:
        if " ERROR" in line:
            error_count = error_count + 1
            error_list.append(line)
    return error_count, error_list

log_dir = sys.argv[0]
analyze_log(log_dir)