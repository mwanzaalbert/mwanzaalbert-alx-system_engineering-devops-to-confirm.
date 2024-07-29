#!/usr/bin/python3
"""
Gather data from an API for a given employee ID and export TODO list progress to JSON
"""

import json
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
    
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        })
    
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, mode='w') as json_file:
        json.dump({str(employee_id): tasks}, json_file)