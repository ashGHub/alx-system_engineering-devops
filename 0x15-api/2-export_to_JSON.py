#!/usr/bin/python3
"""Gather data from an API"""
import json
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
    emp_name = emp.get('username')
    tasks = []
    for tsk in todos:
        tasks.append(
            {
                "task": tsk.get('title'),
                "completed": tsk.get('completed'),
                "username": emp_name
            })
    data = {emp_id: tasks}
    with open(f"{emp_id}.json", mode="w") as json_file:
        json.dump(data, json_file)
