#!/usr/bin/python3
"""
Module to retrieve and display TODO progress for a given employee ID.

This script retrieves TODO progress for a specified employee ID from the
JSONPlaceholder API and displays the completed tasks for that employee along
with their total number.

Example:
    $ python3 0-gather_data_from_an_API.py 1

Attributes:
    None
"""
import sys
import requests


def get_employee_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve employee name: {response.status_code}")
        return None

    user_info = response.json()
    return user_info['name']


def get_employee_todo_progress(employee_id):
    todo_url = (
            f"https://jsonplaceholder.typicode.com/"
            f"users/{employee_id}/todos"
    )
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        print(f"Failed to retrieve data: {todo_response.status_code}")
        return

    todos = todo_response.json()
    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print("Failed to retrieve employee name.")
        return

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    print(f"Employee {employee_name} is done with tasks\
            ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
