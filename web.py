import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('Sample text for show <b>HTML BOLD</b> formatting',
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=' ', label_visibility="hidden",  placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

#st.session_state
