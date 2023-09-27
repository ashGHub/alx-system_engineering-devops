#!/usr/bin/python3
"""Gather data from an API"""
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
    completed = [tsk for tsk in todos if tsk.get('completed') is True]
    emp_name = emp.get('name')
    total_tsk = len(todos)
    com_tsk = len(completed)
    print(f"Employee {emp_name} is done with tasks({com_tsk}/{total_tsk}):")
    for tsk in completed:
        print(f"\t {tsk.get('title')}")
