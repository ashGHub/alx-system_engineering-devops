#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""
    emp_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users/{emp_id}"
    todos_url = f"{base_url}/users/{emp_id}/todos"
    emp = requests.get(users_url).json()
    todos = requests.get(todos_url).json()
    with open(f"{emp_id}.csv", mode="w") as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        for tsk in todos:
            emp_name = emp.get('username')
            comp = tsk.get('completed')
            title = tsk.get('title')
            csv_writer.writerow([emp_id, emp_name, comp, title])
