filepath = 'todos.txt'

def get_todos():
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos):
    with open(filepath, 'w') as file:
        file.writelines(todos)