import streamlit as st
import functions

todos = functions.getTodos()


def addTodo():
    todo = st.session_state["todo"] + '\n'
    todos.append(todo)
    print(todos)
    functions.writeTodos(todos)


st.title('My Todo App')
st.subheader('Write your todos:')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Add a todo',
              on_change=addTodo, key="todo")

st.session_state