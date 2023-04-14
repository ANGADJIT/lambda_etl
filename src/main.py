import requests
from requests import Response
import json
from dotenv import load_dotenv



count: int = 1
completed_count: int = 0
not_completed_count: int = 0

while True:
    response: Response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos/{count}')

    if response.status_code == 404:
        break

    body: str = response.text
    todo: dict = json.loads(body)

    if todo['completed']:
        completed_count += 1

    else:
        not_completed_count += 1

    count += 1

if __name__ == '__main__':
    load_dotenv()
