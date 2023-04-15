import boto3
from os import environ
import json
import constants

s3 = boto3.client('s3')


def upload_todo_as_json(todo: dict, todo_number: int) -> None:

    todo_json_string: str = json.dumps(todo).encode('utf-8')

    s3.put_object(
        Bucket=environ.get(constants.BUCKET_NAME),
        Key=f'landing/todo_{todo_number}.json',
        Body=todo_json_string
    )


def get_all_todo_files() -> list[dict]:

    all_todos: list[dict] = []

    landing_folder_path: str = 'landing/'

    todos = s3.list_objects_v2(Bucket=environ.get(
        constants.BUCKET_NAME), Prefix=landing_folder_path)

    for todo in todos['Contents']:

        if todo['Key'].endswith('.json'):

            file = s3.get_object(Bucket=environ.get(
                constants.BUCKET_NAME), Key=todo['Key'])
            raw_json = file['Body'].read().decode('utf-8')

            all_todos.append(json.loads(raw_json))

    return all_todos


def upload_todos_csv(todos: list[dict], name: str) -> None:
    rows: list[str] = [
        f"{todo['userId']},{todo['id']},{todo['title']},{todo['completed']}\n" for todo in todos]

    csv_string: str = ''

    for row in rows:
        csv_string += row

    s3.put_object(
        Bucket=environ.get(constants.BUCKET_NAME),
        Key=f'processed/todo_{name}.csv',
        Body=csv_string
    )
