#!/usr/bin/python3
"""
Script to export data in the JSON format.
"""
import json
import requests


def export_all_tasks():
    # Fetch user data
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")

        # Fetch tasks data for each user
        todo_data = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId="
                + str(user_id)).json()

        # Format data
        task_list = []
        for task in todo_data:
            task_dict = {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            task_list.append(task_dict)

        # Add tasks to the dictionary
        all_tasks[user_id] = task_list

    # Save data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_tasks()
