def filter_todos(todos: list[dict]) -> dict:
    completed_todos: list[dict] = []
    not_completed_todos: list[dict] = []

    for todo in todos:
        if todo['completed']:
            completed_todos.append(todo)
        else:
            not_completed_todos.append(todo)

    result: dict = {
        'completed_todos': completed_todos,
        'not_completed_todos': not_completed_todos
    }

    return result
