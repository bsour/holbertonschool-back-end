#!/usr/bin/python3
""" This module make beginner level API calls to a dummy data service"""
import requests
import sys


def gather_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{employee_url}/todos"

    response_employee = requests.get(employee_url)
    response_todo = requests.get(todo_url)

    if response_employee.status_code != 200:
        print("Error fetching employee data.")
        return

    if response_todo.status_code != 200:
        print("Error fetching TODOD list data.")
        return

    employee_data = response_employee.json()
    todo_data = response_todo.json()

    employee_name = employee_data["name"].strip()
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    try:
        if not sys.argv[1]:
            pass
    except IndexError:
        sys.exit("This script requires an argument of employee_id number")
