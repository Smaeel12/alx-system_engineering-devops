#!/usr/bin/python3
"""
Module to export employee's TODO progress to a CSV file.

This script retrieves TODO progress for a given employee ID from the
JSONPlaceholder API and exports the data to a CSV file. It includes functions
to retrieve employee information, retrieve TODO progress, and export
the data to a CSV file.

Example:
    $ python3 1-export_to_CSV.py 1

Attributes:
    None
"""
import csv
import requests
import sys


def get_employee_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve employee name: {response.status_code}")
        return None

    user_info = response.json()
    return user_info['name']


def export_to_csv(employee_id, todos):
    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print("Failed to retrieve employee name.")
        return

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(todo['completed']),
                'TASK_TITLE': todo['title']
            })


def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    todos = response.json()
    export_to_csv(employee_id, todos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
