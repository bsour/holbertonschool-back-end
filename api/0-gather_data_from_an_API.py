#!/usr/bin/python3
"""
Gathers data from an API.
"""

import requests
import sys


def gather_data(employee_id):
    """
    Gathers and displays data from an API for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    response_employee = requests.get(employee_url)
    response_todo = requests.get(todo_url)

    if response_employee.status_code != 200:
        print("Error fetching employee data.")
        return

    if response_todo.status_code != 200:
        print("Error fetching TODO list data.")
        return

    employee_data = response_employee.json()
    todo_data = response_todo.json()

    employee_name = employee_data["name"]
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
