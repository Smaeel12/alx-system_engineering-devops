#!/usr/bin/python3
import sys
import requests
import json


def get_employee_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve employee name: {response.status_code}")
        return None

    user_info = response.json()
    return user_info['name']


def export_to_json(employee_id, todos):
    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print("Failed to retrieve employee name.")
        return

    data = {str(employee_id): []}
    for todo in todos:
        data[str(employee_id)].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        })

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return

    todos = response.json()
    export_to_json(employee_id, todos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
