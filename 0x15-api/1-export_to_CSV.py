#!/usr/bin/python3
"""
Gather data from an API for a given employee ID and export TODO list progress to CSV
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    
    user = requests.get("{}/users/{}".format(url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url,
                                                     employee_id)).json()
    
    employee_name = user.get("username")
    
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([employee_id, employee_name,
                                 task.get("completed"), task.get("title")])