#!/usr/bin/python3
"""for a given id return information about their TODO list"""
import csv
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={"userId": user_id}).json()
    user_name = user.get("name")
    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user_name, task.get("completed"),
                             task.get("title")])
