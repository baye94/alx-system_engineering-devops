
#!/usr/bin/python3
"""
A Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress
"""
from argparse import ArgumentParser
from os import path
from requests import get
from sys import argv


mockApi = "https://jsonplaceholder.typicode.com/"


if __name__ == '__main__':

    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('ID', type=int, help="employee ID")
    args = parser.parse_args()
    user = get('/'.join([mockApi, 'users', str(args.id)])).json()
    todo = get('/'.join([mockApi, 'todos']), params={'userId': args.id}).json()
    completed = [task for task in todo if task['NUMBER_OF_DONE_TASKS'] is True]
    print('EMPLOYEE_NAME {} is done with tasks({}/{}):'.format(
        user['EMPLOYEE_NAME'], len(completed), len(todo)))
    print('\n'.join('\t {}'.format(task['title']) for task in completed))
