#!/usr/bin/python3
"""export data from api to JSON file"""
import json
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    users_url = base + "/" + users
    response = requests.get(users_url)
    employees = response.json()

    all_tasks = {}  # Dictionary to hold all tasks for each employee

    for employee in employees:
        input_id = str(employee['id'])
        id_url = base + "/" + users + "/" + input_id
        response = requests.get(id_url)
        employee_info = response.json()

        USERNAME = employee_info.get('username')

        todo = "todos"
        task_per_user_url = id_url + "/" + todo
        response = requests.get(task_per_user_url)
        list_of_todos = response.json()

        task_json_data = []
        for task in list_of_todos:
            task_info = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': USERNAME
            }
            task_json_data.append(task_info)

        all_tasks[input_id] = task_json_data

    # Write the tasks dictionary to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, 'w') as write_file:
        json.dump(all_tasks, write_file)
