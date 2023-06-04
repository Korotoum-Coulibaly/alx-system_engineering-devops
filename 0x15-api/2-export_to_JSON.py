#!/usr/bin/python3
""" Python script that, exports data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    infos = requests.get(url).json()

    with open('{}.json'.format(id), 'w') as json_file:
        tasks = []
        for t in infos:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": user.get("username")})
        data = {"{}".format(id): tasks}
        json.dump(data, json_file)