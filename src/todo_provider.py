import requests
from requests import Response
import logging
import json
from aws import upload_todo_as_json, get_all_todo_files


def upload_todos() -> None:

    url: str = 'https://jsonplaceholder.typicode.com/todos/'

    todo_count = 1

    while True:

        todo: Response = requests.get(f'{url}/{todo_count}')

        if todo.status_code == 404:
            break

        body = todo.text
        todo: dict = json.loads(body)

        upload_todo_as_json(todo=todo, todo_number=todo_count)
        todo_count += 1

        logging.info(f'UPLOADED TODO {todo_count}')


def get_todos():
    return get_all_todo_files()