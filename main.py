import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is", now)

while True:
    user_choice = input("Please choose add, show, edit, complete or exit: ")
    user_choice = user_choice.strip()

    if user_choice.startswith("add"):
        added_item = user_choice[4:]

        todos = functions.get_todos()

        todos.append((added_item + "\n"))

        functions.write_todos(todos)

    elif user_choice.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index+1}-{item.strip('\n')}")

    elif user_choice.startswith("edit"):
        try:
            item_to_edit = int(user_choice[5:])

            todos = functions.get_todos()

            new_item = input("Enter a new todo: ")

            todos[item_to_edit-1] = new_item + '\n'

            functions.write_todos(todos)

        except:
            print("Sorry, invalid command")

    elif user_choice.startswith("complete"):
        try:
            item_to_pop = int(user_choice[9:])

            todos = functions.get_todos()

            todo_to_remove = todos.pop(item_to_pop-1)

            functions.write_todos(todos)

            print(f"{todo_to_remove.strip('\n')} was removed from the list")
        except:
            print("Sorry, invalid command")

    elif "exit" in user_choice:
        break
    else:
        print("Wrong Command")