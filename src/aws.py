import boto3
from os import environ
import json
import constants


def upload_todo_as_file(todo: dict, todo_number: int) -> None:
    s3 = boto3.client('s3')

    todo_json_string: str = json.dumps(todo).encode('utf-8')

    s3.put_object(
        Bucket=environ.get(constants.BUCKET_NAME),
        Key=f'landing/todo_{todo_number}.json',
        Body=todo_json_string
    )

def get_all_todo_files() -> list:
    pass