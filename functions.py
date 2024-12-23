FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read todos from the file and return a list """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos into the file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

