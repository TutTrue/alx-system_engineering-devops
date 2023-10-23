#!/usr/bin/python3
"""for a given id return information about their TODO list"""

import requests
import sys
import csv


if __name__ == '__main__':

    res = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')
    if res.status_code == 200:
        data = res.json()
        tasks = tasks.json()
        with open(f'{sys.argv[1]}.csv', 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in tasks:
                writer.writerow([sys.argv[1], data.get("name"),
                                 task.get("completed"), task.get("title")])
