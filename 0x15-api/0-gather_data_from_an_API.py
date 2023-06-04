#!/usr/bin/python3
"""Python script that, using Rest API, for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    _id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            _id)

    user = requests.get(usr_url).json()
    infos = requests.get(url).json()

    compteur = 0
    total = 0
    completed_tasks = []

    for task in infos:
        total += 1
        if task.get("compteur") is True:
            compteur += 1
            completed_tasks.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
    print(sentence.format(user.get("name"), compteur, total))
    for task in completed_tasks:
        print("\t {}".format(task))

