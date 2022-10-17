#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        EMPLOYEE_NAME = req.json().get("name")
        if EMPLOYEE_NAME is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltsk = len(jreq)
            NUMBER_OF_DONE_TASKS = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtsk.append(t)
            TOTAL_NUMBER_OF_TASKS = len( NUMBER_OF_DONE_TASKS)
            print("Employee {} is done with tasks({}/{}):"
                  .format(EMPLOYEE_NAME, count, alltsk))
            for title in NUMBER_OF_DONE_TASKS:
                print("\t {}".format(title.get("title")))
