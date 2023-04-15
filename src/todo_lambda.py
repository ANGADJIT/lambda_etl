from dotenv import load_dotenv
import todo_provider
import process
from aws import upload_todos_csv
import logging


def process_todos(event, context):
    load_dotenv()

    # upload all todos
    todo_provider.upload_todos()

    # get all todos after uploading files
    todos: list[dict] = todo_provider.get_todos()

    # now filter todos using process
    filtered_todos: dict = process.filter_todos(todos)

    # now upload filtered data as csv
    upload_todos_csv(todos=filtered_todos['completed_todos'], name='completed')
    upload_todos_csv(
        todos=filtered_todos['not_completed_todos'], name='not_completed')

    # end of job
    logging.info('*****END JOB*****')

process_todos(None,None)