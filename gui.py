import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", mode="w") as file:
        pass

sg.theme("Black")

clock_label = sg.Text(text="", key="clock")
label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events= True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label,],
                           [clock_label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window["clock"].update(value=now)
    match event:
        case "Add":
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"

                todos = functions.get_todos()
                index_to_edit = todos.index(todo_to_edit)
                todos[index_to_edit] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]

                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))
        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

window.close()