#!/usr/bin/python3
import requests


"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()


if __name__ == "__main__":
    main()
