#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """"Gather data from an API"""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"
    emps = requests.get(users_url).json()
    todos = requests.get(todos_url).json()
    tasks = []
    data = {}
    for emp in emps:
        emp_id = emp.get('id')
        emp_name = emp.get('username')
        tasks = []
        for tsk in todos:
            if emp_id == tsk.get('userId'):
                tasks.append(
                    {
                        "username": emp_name,
                        "task": tsk.get('title'),
                        "completed": tsk.get('completed')
                    })
        data[emp_id] = tasks
    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(data, json_file)
