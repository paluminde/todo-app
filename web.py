import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)

def remove_todo():
    for todo in todos:
        if st.session_state[todo]:
            todos.remove(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.write("An app to increase productivity")

for todo in todos:
    st.checkbox(todo, key=todo, on_change=remove_todo)


st.text_input(label="Enter Todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
