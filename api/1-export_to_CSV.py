#!/usr/bin/python3
"""This script retrieves and processes data from the JSONPlaceholder API to
gather information about an employee's tasks and exports it in CSV format. """
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <integer>")
        sys.exit(1)

    # URL builder
    base = "https://jsonplaceholder.typicode.com"
    users = "users"
    employee_id = str(sys.argv[1])
    api_url = base + "/" + users + "/" + employee_id
    response = requests.get(api_url)

    # employee name
    employee_info = response.json()
    EMPLOYEE_ID = employee_info.get('id')
    EMPLOYEE_USERNAME = employee_info.get('username')

    # number of tasks for employee
    todo = "todos"
    task_per_user_url = api_url + "/" + todo
    response = requests.get(task_per_user_url)
    list_of_todos = response.json()

    # Extract task information for CSV export
    csv_data = []
    for task in list_of_todos:
        task_completed_status = task.get('completed')
        task_title = task.get('title')
        csv_data.append([EMPLOYEE_ID, EMPLOYEE_USERNAME,
                         str(task_completed_status), task_title])

    # Export data to CSV file
    csv_file_name = f"{EMPLOYEE_ID}.csv"
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"CSV file '{csv_file_name}' has been created.")
