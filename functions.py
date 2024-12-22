def get_todos(filepath="todos.txt"):
    """ Read todos from the file and return a list """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write todos into the file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
