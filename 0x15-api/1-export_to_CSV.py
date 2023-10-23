#!/usr/bin/python3
"""for a given id return information about their TODO list"""

import csv
import sys
import requests


if __name__ == '__main__':

    user_id = sys.argv[1]
    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    if res.status_code == 200:
        data = res.json()
        tasks = tasks.json()
        user_name = data.get("name")
        with open(f'{user_id}.csv', 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([user_id, user_name,
                                 task.get("completed"), task.get("title")])
