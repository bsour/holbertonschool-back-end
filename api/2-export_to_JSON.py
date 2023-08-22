#!/usr/bin/python3
"""export data from api to JSON file"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # URL builder
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    users_url = base + "/" + users
    response = requests.get(users_url)
    employee_info = response.json()

    # specific employee info
    input_id = str(sys.argv[1])
    id_url = base + "/" + users + "/" + input_id
    response = requests.get(id_url)
    employee_info = response.json()

    # employee username
    USERNAME = employee_info.get('username')

    # number of tasks for employee
    todo = "todos"
    task_per_user_url = id_url + "/" + todo
    response = requests.get(task_per_user_url)
    list_of_todos = response.json()

    # Calculate the number of completed tasks
    NUMBER_OF_DONE_TASKS = sum(
        1 for task in list_of_todos if task.get('completed')
    )

    # Prepare JSON data
    task_json_data = []
    for task in list_of_todos:
        task_info = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': USERNAME
        }
        task_json_data.append(task_info)

    # Export data to JSON
    filename_json = input_id + ".json"
    with open(filename_json, 'w') as jsonfile:
        json.dump({
            "USER_ID": input_id,
            "NUMBER_OF_DONE_TASKS": NUMBER_OF_DONE_TASKS,
            "tasks": task_json_data
        }, jsonfile, indent=4)
