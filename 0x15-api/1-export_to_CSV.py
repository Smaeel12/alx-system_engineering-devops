#!/usr/bin/python3
"""
exports employee info to csv
"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    USER_ID = argv[1]
    request = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    )
    USERNAME = request.json()["username"]
    requestTasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={USER_ID}"
    )
    with open(f"{USER_ID}.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for dictionary in requestTasks.json():
            data = [
                str(USER_ID),
                str(USERNAME),
                str(dictionary.get("completed")),
                str(dictionary.get("title")),
            ]
            writer.writerow(data)
