import streamlit as st
import functions

#def add_todo():
   # todo = st.session_state["new_todo"]
    #todos.append(todo) + '\n'
   # functions.write_todos(todos)

todos = functions.get_todos()

st.title("My To-Do App")
st.write("An app to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...",)