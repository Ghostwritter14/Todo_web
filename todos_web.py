import streamlit as st
import functions

todos = functions.get_todos()
st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("App created by Soham..")
st.write("<b>This app is used to check your daily tasks from anywhere.</b>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a task you want to do today: ",
              placeholder="Add a new task",
              on_change=add_todo, key='new_todo')


